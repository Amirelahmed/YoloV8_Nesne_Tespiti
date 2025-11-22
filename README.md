# YOLOv8 ile Nesne Tespiti + PyQt5 GUI Projesi

Bu proje, YOLOv8 modeli kullanarak görüntüler üzerinde nesne tespiti yapılmasını ve sonuçların PyQt5 tabanlı bir masaüstü arayüzde gösterilmesini sağlar.

---

## 📌 Proje İçeriği

- Kendi oluşturduğum **araç (car)** veri seti YOLO formatında etiketlendi  
- YOLOv8 modeli Google Colab üzerinde eğitildi  
- Eğitim sonunda **best.pt** modeli elde edildi  
- PyQt5 ile GUI geliştirildi:
  - Görsel seçme  
  - YOLO modeli ile nesne tespiti  
  - Bounding box çizimi  
  - Sonuç görselinin ekranda gösterilmesi  

---

## 📁 Proje Dosyaları
yolo_gui/
 ├── gui_app.py                # PyQt5 arayüz kodu
 ├── best.pt                   # Eğitilen YOLOv8 modeli
 └── predictions/              # Test sonuçlarının kaydedildiği klasör
      ├── car_02.jpg
      ├── car_08.jpg
      └── diğer sonuç görüntüleri
      
---

---
## 🧠 YOLOv8 Eğitim Bilgileri

Google Colab üzerinde şu adımlar uygulandı:

- Veri seti yüklendi (images/train – images/val – labels/train – labels/val)
- Etiketler düzenlendi (tüm sınıflar **car → 0**)
- `data.yaml` dosyası oluşturuldu
- YOLOv8s modeli **50 epoch** boyunca eğitildi


### Eğitim kodu:

```python
from ultralytics import YOLO
model = YOLO("yolov8s.pt")
model.train(data="/content/dataset/data.yaml", epochs=50, imgsz=640, batch=8)

📸 Örnek Tespit Sonucu
Aşağıdaki görüntü modelin başarıyla çizdiği bounding box örneklerinden biridir:
![Detection Result](https://raw.githubusercontent.com/Amirelahmed/YoloV8_Nesne_Tespiti/f1fbf3619be767c6e2dc57c4a54c875bdfbf5e46/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202025-11-22%20233358.png)


👤 Geliştirici Bilgileri
Ad Soyad: Amir Elahmed
Ders: BLG407 – Makine Öğrenmesi
Öğretim Üyesi: Doç. Dr. Sinan Uğuz
      
