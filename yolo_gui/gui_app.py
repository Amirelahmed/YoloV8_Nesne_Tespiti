# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtCore import Qt
# from ultralytics import YOLO
# import os


# class YoloGUI(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("YOLOv8 Object Detection - Car Detector")
#         self.setGeometry(200, 200, 800, 600)

#         # تحميل النموذج
#         self.model = YOLO("best.pt")

#         # الواجهة
#         self.image_label = QLabel("No Image Selected")
#         self.image_label.setStyleSheet("border: 2px dashed gray; padding: 10px;")
#         self.image_label.setAlignment(Qt.AlignCenter)

#         self.btn_select = QPushButton("Select Image")
#         self.btn_select.clicked.connect(self.select_image)

#         self.btn_detect = QPushButton("Detect")
#         self.btn_detect.clicked.connect(self.detect)

#         layout = QVBoxLayout()
#         layout.addWidget(self.image_label)
#         layout.addWidget(self.btn_select)
#         layout.addWidget(self.btn_detect)

#         self.setLayout(layout)

#         self.image_path = None

#     def select_image(self):
#         file_path, _ = QFileDialog.getOpenFileName(
#             self,
#             "Choose Image",
#             "",
#             "Images (*.jpg *.png *.jpeg)"
#         )
#         if file_path:
#             self.image_path = file_path
#             pixmap = QPixmap(file_path)
#             pixmap = pixmap.scaled(600, 400, Qt.KeepAspectRatio)
#             self.image_label.setPixmap(pixmap)

#     def detect(self):
#         if self.image_path is None:
#             self.image_label.setText("Please select an image first!")
#             return

#         results = self.model(self.image_path)

#         # مجلد حفظ النتائج
#         save_dir = "predictions"
#         os.makedirs(save_dir, exist_ok=True)

#         # حفظ ملف الصورة الناتجة (نفس الاسم الأصلي)
#         output_path = os.path.join(save_dir, os.path.basename(self.image_path))

#         # حفظ النتيجة
#         results[0].save(output_path)

#         # عرض الصورة الناتجة
#         pixmap = QPixmap(output_path)
#         pixmap = pixmap.scaled(600, 400, Qt.KeepAspectRatio)
#         self.image_label.setPixmap(pixmap)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     gui = YoloGUI()
#     gui.show()
#     sys.exit(app.exec_())


import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from ultralytics import YOLO
import numpy as np

class YoloGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YOLOv8 Object Detection - GUI")
        self.setGeometry(200, 200, 900, 700)

        self.model = YOLO("best.pt")

        self.image_label = QLabel("No Image Selected")
        self.image_label.setStyleSheet("border: 2px dashed gray; padding: 10px;")
        self.image_label.setAlignment(Qt.AlignCenter)

        self.btn_select = QPushButton("Select Image")
        self.btn_select.clicked.connect(self.select_image)

        self.btn_detect = QPushButton("Detect")
        self.btn_detect.clicked.connect(self.detect)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.btn_select)
        layout.addWidget(self.btn_detect)

        self.setLayout(layout)
        self.image_path = None

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Choose Image", "", "Images (*.jpg *.jpeg *.png)")
        if file_path:
            self.image_path = file_path
            pixmap = QPixmap(file_path).scaled(700, 500, Qt.KeepAspectRatio)
            self.image_label.setPixmap(pixmap)

    def detect(self):
        if not self.image_path:
            self.image_label.setText("Please select an image first!")
            return

        # YOLO prediction
        results = self.model(self.image_path)[0]
        img = cv2.imread(self.image_path)

        # Draw boxes using results
        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            label = f"{results.names[cls]} {conf:.2f}"

            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
            cv2.putText(img, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

        # Convert OpenCV image → QPixmap
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = img_rgb.shape
        qimg = QImage(img_rgb.data, w, h, ch * w, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg).scaled(700, 500, Qt.KeepAspectRatio)

        self.image_label.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YoloGUI()
    window.show()
    sys.exit(app.exec_())
