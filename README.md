# 🚗 YOLOv8 ile Nesne Tespiti + PyQt5 GUI Projesi

Bu proje, YOLOv8 modeli ile görüntüler üzerinde **araç (car)** tespiti yapar ve sonuçları **PyQt5 tabanlı GUI** arayüzünde kullanıcıya gösterir.

---

## 📌 Proje Özeti

- 100 adet araba görüntüsü toplandı
- Tüm görüntüler YOLO formatında etiketlendi (`.txt`)
- YOLOv8 modeli Google Colab üzerinde eğitildi
- Eğitim sonucunda **best.pt** ağırlık dosyası elde edildi
- PyQt5 ile GUI arayüz geliştirildi:
  - Görsel seçme
  - YOLO modelini çalıştırma
  - Bounding box çizimi
  - Sonuç görüntüsünü ekranda gösterme

---

## 📁 Proje Dosyaları
yolo_gui/
├── gui_app.py # PyQt5 arayüz kodu
├── best.pt # Eğitilen YOLOv8 modeli
└── predictions/ # Test sonuç görüntüleri
├── car_02.jpg
├── car_08.jpg
└── diğer örnekler

---

## 🧠 YOLOv8 Eğitim Bilgileri

Google Colab üzerinde uygulanan adımlar:

- Veri seti yüklendi:  
  `images/train - images/val - labels/train - labels/val`
- Etiketler düzenlendi (tüm sınıflar **car → 0**)
- `data.yaml` oluşturuldu
- YOLOv8s modeli **50 epoch** boyunca eğitildi

### 🖥️ Eğitim Kodu:

```python
from ultralytics import YOLO
model = YOLO("yolov8s.pt")
model.train(data="/content/dataset/data.yaml", epochs=50, imgsz=640, batch=8)
```python

📸 Örnek Tespit Sonucu

Aşağıdaki görüntü modelin başarıyla tespit yaptığı bir örnektir:

![Detection Result](https://raw.githubusercontent.com/Amirelahmed/YoloV8_Nesne_Tespiti/f1fbf3619be767c6e2dc57c4a54c875bdfbf5e46/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202025-11-22%20233358.png)


👤 Geliştirici Bilgileri

Ad Soyad: Amir Elahmed
Ders: BLG407 – Makine Öğrenmesi
Öğretim Üyesi: Doç. Dr. Sinan Uğuz
