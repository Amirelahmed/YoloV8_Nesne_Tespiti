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
import os
from PIL import Image  # WEBP dönüşümü için


SUPPORTED_FORMATS = ["jpg", "jpeg", "png", "webp", "bmp", "tiff"]


class YOLOApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YOLOv8 Saat / Fare Tespit Uygulaması")
        self.setGeometry(200, 100, 1100, 650)

        # Model yükleme
        model_path = "best.pt"
        if not os.path.exists(model_path):
            QMessageBox.critical(self, "Hata", "best.pt dosyası bulunamadı!")
            sys.exit()
        self.model = YOLO(model_path)

        self.image_path = None
        self.result_img = None

        self.init_ui()

    def init_ui(self):
        self.label_input = QLabel("Girdi Görseli", self)
        self.label_output = QLabel("Tespit Sonucu", self)

        for lbl in (self.label_input, self.label_output):
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setStyleSheet("font-size: 18px; font-weight: bold; color: #333;")

        self.img_input = QLabel(self)
        self.img_output = QLabel(self)

        for box in (self.img_input, self.img_output):
            box.setFixedSize(450, 450)
            box.setAlignment(Qt.AlignCenter)
            box.setStyleSheet("background-color: #ddd; border: 2px solid #aaa; border-radius: 10px;")

        self.btn_load = QPushButton("Resim Seç")
        self.btn_detect = QPushButton("Tespit Yap")
        self.btn_save = QPushButton("Sonucu Kaydet")

        self.btn_load.setStyleSheet(self.btn_style("#3498db"))
        self.btn_detect.setStyleSheet(self.btn_style("#27ae60"))
        self.btn_save.setStyleSheet(self.btn_style("#f39c12"))

        self.btn_load.clicked.connect(self.load_image)
        self.btn_detect.clicked.connect(self.run_detection)
        self.btn_save.clicked.connect(self.save_output)

        h_images = QHBoxLayout()
        h_images.addWidget(self.img_input)
        h_images.addWidget(self.img_output)

        h_buttons = QHBoxLayout()
        h_buttons.addWidget(self.btn_load)
        h_buttons.addWidget(self.btn_detect)
        h_buttons.addWidget(self.btn_save)

        v_main = QVBoxLayout()
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

    def convert_if_webp(self, path):
        """WEBP → JPEG dönüştürme"""
        ext = path.split(".")[-1].lower()
        if ext != "webp":
            return path

        img = Image.open(path).convert("RGB")
        new_path = path.replace(".webp", ".jpg")
        img.save(new_path, "JPEG")
        return new_path

    def load_image(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Resim Seç",
            "",
            "Resimler (*.jpg *.jpeg *.png *.webp *.bmp *.tiff)"
        )

        if not path:
            return

        # WEBP dosyalarını dönüştür
        fixed_path = self.convert_if_webp(path)

        self.image_path = fixed_path
        pix = QPixmap(fixed_path).scaled(450, 450, Qt.KeepAspectRatio)
        self.img_input.setPixmap(pix)

    def run_detection(self):
        if not self.image_path:
            QMessageBox.warning(self, "Uyarı", "Önce bir resim seçmelisiniz!")
            return

        results = self.model(self.image_path)[0]
        img = cv2.imread(self.image_path)

        annotated = results.plot()
        self.result_img = annotated

        qimg = QImage(
            annotated.data,
            annotated.shape[1],
            annotated.shape[0],
            annotated.shape[1] * 3,
            QImage.Format_RGB888
        ).rgbSwapped()

        self.img_output.setPixmap(QPixmap.fromImage(qimg).scaled(450, 450, Qt.KeepAspectRatio))

    def save_output(self):
        if self.result_img is None:
            QMessageBox.warning(self, "Uyarı", "Kaydedilecek bir sonuç yok!")
            return

        save_path, _ = QFileDialog.getSaveFileName(self, "Kaydet", "", "PNG (*.png)")
        if save_path:
            cv2.imwrite(save_path, self.result_img)
            QMessageBox.information(self, "Başarılı", "Görsel kaydedildi!")


app = QApplication(sys.argv)
window = YOLOApp()
window.show()
sys.exit(app.exec_())
