# YOLOv8 Saat & Fare Nesne Tespiti – PyQt5 Masaüstü Uygulaması

Bu proje, BLG407 Makine Öğrenmesi dersi kapsamında geliştirilmiş olup YOLOv8 modeli kullanılarak **Saat (Clock)** ve **Fare (Mouse)** nesnelerinin tespit edilmesini amaçlamaktadır.  
Proje için kullanılan tüm görüntüler **kendi telefonumla çektiğim özgün fotoğraflardan** oluşmaktadır.

---

# 📸 Veri Seti (Tarafımdan Çekilmiştir)

Bu projede kullanılan veri seti tamamen bana ait olup farklı açılar, ışık koşulları ve arka plan çeşitliliği dikkate alınarak oluşturulmuştur.

| Sınıf | Görüntü Sayısı |
|-------|----------------|
| **Saat (Clock)** | 110 görüntü |
| **Fare (Mouse)** | 110 görüntü |
| **Toplam** | **220 görüntü** |

Tüm görüntüler LabelImg aracıyla **YOLO formatında** manuel olarak etiketlenmiştir.

### 📌 YOLO Formatı Örneği

```python
<class_id> <x_center> <y_center> <width> <height>
```
---


---

# 🧠 YOLOv8 Model Eğitimi

Model, Google Colab üzerinde YOLOv8s tabanlı mimari kullanılarak eğitilmiştir.  
Eğitim sırasında veri artırma (augmentation), 640×640 çözünürlük ve uygun hiperparametreler uygulanmıştır.

### 🟦 Örnek Eğitim Kodu:
```python
from ultralytics import YOLO

model = YOLO("yolov8s.pt")
model.train(
    data="/content/dataset/data.yaml",
    epochs=60,
    imgsz=640,
    batch=8
)
```

Eğitim sonucunda elde edilen best.pt dosyası masaüstü uygulamasında kullanılmıştır.

# 📂 Dosya Yapısı

```plaintext
YoloV8_Nesne_Tespiti/
│
├── dataset/                          # Tarafımdan çekilen ve etiketlenen 220 görüntü
│   ├── images/
│   │   ├── train/
│   │   └── val/
│   └── labels/
│       ├── train/
│       └── val/
│
├── images/                           # Model test sonuç görselleri
│   ├── Saat/
│   │   ├── saat_1.png
│   │   └── saat_2.png
│   ├── Fare/
│   │   ├── fare_1.png
│   │   └── fare_2.png
│   └── Birlikte/
│       ├── birlikte_1.png
│       └── birlikte_2.png
│
├── best.pt                           # Eğitilmiş YOLOv8 model dosyası
├── gui.py                            # PyQt5 masaüstü tespit arayüzü
├── yolo_training.ipynb               # YOLOv8 eğitim notebook dosyası
└── README.md                         # Proje dokümantasyonu
```

🖥️ PyQt5 Masaüstü Uygulaması

Geliştirilen GUI, kullanıcıya kolay ve anlaşılır bir nesne tespiti deneyimi sunmaktadır.

### Uygulama Özellikleri

Her formatta görsel yükleme (JPG, PNG, WEBP, BMP, TIFF)

WEBP → JPG otomatik dönüşümü

YOLOv8 ile anında nesne tespiti

Orijinal ve tespit edilmiş görüntülerin yan yana gösterilmesi

Çıktı görselini kaydetme özelliği

### Çalıştırma Komutları
```python
pip install pyqt5 ultralytics opencv-python pillow
python gui.py
```
### Model Test Sonuçları

Aşağıdaki örnek çıktılar, eğitilen modelin gerçek görüntüler üzerinde verdiği tahmin sonuçlarını göstermektedir.
Bu görsellerin tamamı images/ klasörü içinde de bulunmaktadır.

## ⌚ 1. Saat (Clock) Tespit Sonuçları – 2 Örnek
### Örnek 1 – Saat düzgün açıdan çekilmiş, model yüksek doğrulukla tespit etmiştir.
![Saat 1](https://github.com/Amirelahmed/YoloV8_Nesne_Tespiti/blob/248fd7380760f01e573ed880f668d5ebc0cc953d/images/Saat/saat_1.png)

### Örnek 2 – Farklı ışıklandırma altında saat nesnesi başarıyla tespit edilmiştir.
![Saat 2](https://github.com/Amirelahmed/YoloV8_Nesne_Tespiti/blob/248fd7380760f01e573ed880f668d5ebc0cc953d/images/Saat/saat_2.png)

## 🖱️ 2. Fare (Mouse) Tespit Sonuçları – 2 Örnek
# Örnek 1 – Fare halı üzerinde küçük bir nesne olmasına rağmen doğru tespit edilmiştir.
![Fare 1](https://github.com/Amirelahmed/YoloV8_Nesne_Tespiti/blob/e7a147010f06dfb3f27d1907667470e973678dc6/images/Fare/fare_1.png)

### Örnek 2 – Farklı zemin dokusunda fareyi başarıyla algılamıştır.
![Fare 2](https://github.com/Amirelahmed/YoloV8_Nesne_Tespiti/blob/e7a147010f06dfb3f27d1907667470e973678dc6/images/Fare/fare_2.png?raw=true)


## 🕒🖱️ 3. Karışık Sahne (Saat + Fare) – 2 Örnek
### Örnek 1 – Tek sahnede yalnızca saat bulunan görüntü başarılı şekilde tespit edilmiştir.
![Birlikte 1](https://github.com/Amirelahmed/YoloV8_Nesne_Tespiti/blob/248fd7380760f01e573ed880f668d5ebc0cc953d/images/Birlikte/birlikte_1.png)

### Örnek 2 – Hem saat hem fare tek kare içinde olup model her iki nesneyi de doğru tanımıştır.
![Birlikte 2](https://github.com/Amirelahmed/YoloV8_Nesne_Tespiti/blob/248fd7380760f01e573ed880f668d5ebc0cc953d/images/Birlikte/birlikte_2.png)

---
# 👤 Hazırlayan
**Amir Elahmed**  
BLG407 – Makine Öğrenmesi  
YOLOv8 Nesne Tespiti Projesi
