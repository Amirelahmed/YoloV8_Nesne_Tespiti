# YOLOv8 ile Nesne Tespiti + PyQt5 GUI Projesi

Bu proje, YOLOv8 modeli ile araç (car) tespiti yapan bir makine öğrenmesi projesidir.  
Google Colab üzerinde model eğitilmiş ve PyQt5 ile masaüstü bir arayüz geliştirilmiştir.

---

## 📁 Proje Dosyaları

```
yolo_gui/
 ├── gui_app.py                # PyQt5 arayüz kodu
 ├── best.pt                   # Eğitilen YOLOv8 modeli
 └── predictions/              # Test sonuç görselleri
      ├── car_02.jpg
      ├── car_08.jpg
```

---

## 🧠 YOLOv8 Eğitim Süreci

Aşağıdaki kod kullanılarak Google Colab üzerinde eğitim yapılmıştır:

### 📌 Eğitim Kodu:

```python
from ultralytics import YOLO

model = YOLO("yolov8s.pt")
model.train(
    data="/content/dataset/data.yaml",
    epochs=50,
    imgsz=640,
    batch=8
)
```

### 📊 Eğitim Sonuç Görseli
Aşağıda eğitimden elde edilen sonuçlar gösterilmektedir:

![Training Results](https://github.com/Amirelahmed/YoloV8_Nesne_Tespiti/blob/main/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202025-11-22%20233358.png?raw=true)

---

## 🖥️ PyQt5 GUI Özellikleri

- Görsel seçme  
- YOLO modeli ile nesne tespiti  
- Bounding box çizimi  
- İşlenen görüntüyü ekranda gösterme  

---

## 👤 Geliştirici Bilgileri

**Ad Soyad:** Amir Elahmed  
**Ders:** BLG407 – Makine Öğrenmesi  
**Öğretim Üyesi:** Doç. Dr. Sinan Uğuz  

---

