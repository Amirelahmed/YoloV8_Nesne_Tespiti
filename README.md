# 🚀 YOLOv8 Car & Person Detection – PyQt5 GUI

Bu proje, YOLOv8 derin öğrenme modeli kullanılarak **Araba (Car)** ve **İnsan (Person)** tespiti yapan gelişmiş bir bilgisayarlı görü uygulamasıdır.  
Model Google Colab üzerinde eğitilmiş ve PyQt5 kullanılarak masaüstü bir arayüz geliştirilmiştir.

---

# 📂 Proje Yapısı

| Klasör / Dosya     | Açıklama |
|--------------------|----------|
| **gui_app.py**     | PyQt5 arayüz uygulaması |
| **best.pt**        | Eğitilmiş YOLOv8 modeli |
| **predictions/**   | Test sonuç görüntüleri |
| **dataset/**       | Eğitim veri seti |
| **README.md**      | Proje açıklama dosyası |

---

# 🧠 YOLOv8 Model Eğitimi

| Adım | Açıklama |
|------|----------|
| **1️⃣ Gerekli kütüphaneleri yükleyin** | `pip install ultralytics` |
| **2️⃣ Modeli eğitin** | Aşağıdaki kod Colab üzerinde kullanıldı |

### 📌 Eğitim Kodu

```python
from ultralytics import YOLO

model = YOLO("yolov8s.pt")  # Pretrained model
model.train(
    data="/content/dataset/data.yaml",
    epochs=50,
    imgsz=640,
    batch=8
)

📸 Model Sonuçları

Aşağıda modelin gerçek görüntüler üzerinde elde ettiği tespit sonuçları bulunmaktadır.

🚗 1. Araç (Car) Tespit Sonuçları
✔ Örnek 1

✔ Örnek 2

🧍‍♂️ 2. İnsan (Person) Tespit Sonuçları
✔ Örnek 1

🚗🧍 3. Karışık Sahne (Araç + İnsan) Tespiti
✔ Örnek 1

✔ Örnek 2

🖥️ PyQt5 Masaüstü Arayüz

Bu GUI uygulaması ile kullanıcı:

📤 Görüntü yükleyebilir

🤖 YOLOv8 modeliyle tespit yapabilir

🖼️ Önce / Sonra görüntüsünü yan yana görebilir

💾 Sonuç görüntüsünü kaydedebilir

▶️ Uygulamayı Çalıştırma
Adım	Komut
Gerekli kütüphaneler	pip install pyqt5 ultralytics opencv-python
Uygulamayı başlat	python gui_app.py
Model dosyası	best.pt ile aynı klasörde olmalı

👨‍💻 Geliştirici Bilgileri

Ad Soyad: Amir Elahmed
Ders: BLG407 – Makine Öğrenmesi
Öğretim Üyesi: Doç. Dr. Sinan Uğuz

⭐ Proje Tamamlandı

Bu repo, YOLOv8 nesne tespiti ve PyQt5 GUI entegrasyonu için mükemmel bir örnek niteliğindedir.
Model başarıyla eğitilmiş, test edilmiş ve masaüstü arayüz ile entegre edilmiştir.

