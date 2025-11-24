import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QFileDialog,
    QHBoxLayout, QVBoxLayout, QMessageBox
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from ultralytics import YOLO
import cv2
import numpy as np

class YOLOApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YOLOv8 Car & Person Detector")
        self.setGeometry(200, 100, 1100, 650)

        self.model = YOLO("best.pt")   # ← ضع هنا مسار النموذج المدرب

        # GUI Layout
        self.init_ui()

        self.image_path = None
        self.result_img = None

    def init_ui(self):
        # Labels
        self.label_input = QLabel("Input Image", self)
        self.label_output = QLabel("Detection Result", self)

        for lbl in (self.label_input, self.label_output):
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setStyleSheet("font-size: 18px; font-weight: bold; color: #444;")

        # Image containers
        self.img_input = QLabel(self)
        self.img_output = QLabel(self)
        for img in (self.img_input, self.img_output):
            img.setFixedSize(450, 450)
            img.setStyleSheet("background-color: #eee; border: 2px solid #ccc; border-radius: 8px;")
            img.setAlignment(Qt.AlignCenter)

        # Buttons
        self.btn_load = QPushButton("Select Image")
        self.btn_detect = QPushButton("Run Detection")
        self.btn_save = QPushButton("Save Output")

        self.btn_load.setStyleSheet(self.btn_style("#3498db"))
        self.btn_detect.setStyleSheet(self.btn_style("#27ae60"))
        self.btn_save.setStyleSheet(self.btn_style("#f39c12"))

        self.btn_load.clicked.connect(self.load_image)
        self.btn_detect.clicked.connect(self.run_detection)
        self.btn_save.clicked.connect(self.save_output)

        # Layouts
        h_images = QHBoxLayout()
        h_images.addWidget(self.img_input)
        h_images.addWidget(self.img_output)

        h_buttons = QHBoxLayout()
        h_buttons.addWidget(self.btn_load)
        h_buttons.addWidget(self.btn_detect)
        h_buttons.addWidget(self.btn_save)

        v_main = QVBoxLayout()
        v_main.addWidget(self.label_input)
        v_main.addWidget(self.label_output)
        v_main.addLayout(h_images)
        v_main.addLayout(h_buttons)

        self.setLayout(v_main)

    def btn_style(self, color):
        return f"""
            QPushButton {{
                background-color: {color};
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 8px;
            }}
            QPushButton:hover {{
                background-color: #222;
            }}
        """

    def load_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.jpg *.png)")
        if path:
            self.image_path = path
            pix = QPixmap(path).scaled(450, 450, Qt.KeepAspectRatio)
            self.img_input.setPixmap(pix)

    def run_detection(self):
        if not self.image_path:
            QMessageBox.warning(self, "Warning", "Select an image first!")
            return

        results = self.model(self.image_path)[0]
        img = cv2.imread(self.image_path)
        annotated = results.plot()

        self.result_img = annotated
        qimg = QImage(
            annotated.data, annotated.shape[1], annotated.shape[0],
            annotated.shape[1] * 3, QImage.Format_RGB888
        ).rgbSwapped()

        self.img_output.setPixmap(QPixmap.fromImage(qimg).scaled(450, 450, Qt.KeepAspectRatio))

    def save_output(self):
        if self.result_img is None:
            QMessageBox.warning(self, "Warning", "No output to save!")
            return

        save_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG Files (*.png)")
        if save_path:
            cv2.imwrite(save_path, self.result_img)
            QMessageBox.information(self, "Saved", "Output image saved successfully!")

app = QApplication(sys.argv)
window = YOLOApp()
window.show()
sys.exit(app.exec_())
