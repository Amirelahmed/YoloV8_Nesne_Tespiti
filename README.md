🚀 YOLOv8 ile Araç & İnsan Tespiti + PyQt5 Masaüstü Uygulaması

Bu proje, YOLOv8 derin öğrenme modeli kullanılarak araç (car) ve insan (person) algılama sistemi geliştirmeyi amaçlayan bir makine öğrenmesi uygulamasıdır.
Model Google Colab üzerinde eğitilmiş olup sonuçlar PyQt5 tabanlı modern bir arayüz ile kullanıcıya sunulmaktadır.

📂 Proje Yapısı
YOLOv8_Detection_Project/
 ├── gui_app.py                # PyQt5 arayüz uygulaması
 ├── best.pt                   # Eğitilen YOLOv8 özel modeli
 ├── README.md                 # Proje dokümantasyonu
 └── predictions/              # Test sonuç görselleri
      ├── car_02.jpg
      ├── car_08.jpg

🧠 YOLOv8 Model Eğitimi

Model, Google Colab üzerinde aşağıdaki kodlarla eğitilmiştir:

from ultralytics import YOLO

model = YOLO("yolov8s.pt")
model.train(
    data="/content/dataset/data.yaml",
    epochs=50,
    imgsz=640,
    batch=8
)

📈 Eğitim Sonuç Özeti

Eğitim sonunda elde edilen bazı önemli metrikler:

Precision: Yüksek

Recall: Yüksek

mAP50: Başarılı

mAP50-95: İyi seviyede

Model özellikle araç ve insan sınıflarında güçlü bir performans sağlamaktadır.

📊 Eğitim Sonuç Görselleri

Aşağıda modelin farklı görüntülerdeki performansı gösterilmektedir:

🚗 Araç tespiti örneği

🚙 Farklı bir sahnede YOLOv8 tespiti

🖥️ PyQt5 Arayüz Uygulaması

Arayüz uygulaması kullanıcıya kolay ve modern bir kullanım deneyimi sunar.

⭐ Özellikler:

📁 Görsel seçme

🔍 YOLOv8 ile nesne tespiti

🖼️ İşlenmiş görüntüyü ekranda gösterme

📦 Sonuç görselini kaydetme

🎨 Estetik, sade ve kullanıcı dostu tasarım

🖼️ Arayüzden Örnek

(Buraya ekran görüntüsü ekleyebilirsin.)

📌 Kullanım
1️⃣ Gerekli kütüphaneleri yükleyin:
pip install ultralytics
pip install pyqt5
pip install opencv-python

2️⃣ Uygulamayı çalıştırın:
python gui_app.py

🎯 Projenin Amacı

Bu proje kapsamında:

Derin öğrenme tekniklerini kullanarak nesne tespiti yapılmıştır

YOLOv8 gibi modern ve endüstri-standardı bir model kullanılmıştır

Kişiye özel GUI geliştirilerek model çıktıları görsel olarak sunulmuştur

Model hem araç hem de insan sınıflarında yüksek doğruluk göstermektedir

👨‍💻 Geliştirici Bilgileri
Bilgi	Detay
Ad Soyad	Amir Elahmed
Ders	BLG407 – Makine Öğrenmesi
Öğretim Üyesi	Doç. Dr. Sinan Uğuz
Proje	YOLOv8 Nesne Tespiti + PyQt5 GUI
✅ Sonuç

Bu çalışma, YOLOv8 modeli ve PyQt5 arayüzü sayesinde hem akademik hem de uygulamalı bir makine öğrenmesi projesi olarak güçlü ve profesyonel bir örnek oluşturmaktadır.
Model, gerçek sahne görüntülerinde yüksek doğrulukla araç ve insanları başarıyla tespit etmektedir.
