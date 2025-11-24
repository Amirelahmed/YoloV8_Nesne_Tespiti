# 🚀 YOLOv8 Car & Person Detection – PyQt5 GUI

Bu proje, YOLOv8 derin öğrenme modeli kullanılarak **Araç (Car)** ve **İnsan (Person)** tespiti yapan gelişmiş bir bilgisayarlı görü uygulamasıdır.  
Model Google Colab üzerinde eğitilmiş ve sonuçlar PyQt5 masaüstü uygulaması ile sunulmuştur.

---

# 📂 Proje Yapısı

| Klasör / Dosya | Açıklama |
|----------------|----------|
| `gui_app.py`   | PyQt5 GUI arayüzü |
| `best.pt`      | Eğitilmiş YOLOv8 model dosyası |
| `predictions/` | Tespit örnek görüntüleri |
| `dataset/`     | Eğitim veri seti |
| `README.md`    | Proje açıklama dosyası |

---

# 🧠 YOLOv8 Model Eğitimi

| Adım | Açıklama |
|------|----------|
| **1️⃣ Gerekli kütüphaneleri yükleyin** | `pip install ultralytics` |
| **2️⃣ Modeli eğitin** | Google Colab üzerinde aşağıdaki kod kullanıldı |

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
```

📸 Model Sonuçları

Aşağıda modelin eğitim sonrası gerçek görüntüler üzerindeki tespit performansı gösterilmiştir.
Her görselin üstünde kısa açıklama bulunmaktadır.


## 🚗 1. Araç (Car) Tespit Sonuçları  
### ✔ Örnek 1 — Otopark üzerinde yoğun araç tespiti

Bu görselde model, yukarıdan çekilmiş bir otopark görüntüsünde tüm araçları yüksek doğrulukla tespit etmektedir.

![Detection Result](https://github.com/Amirelahmed/YoloV8_Nesne_Tespiti/blob/aacd920cb6cd4f0349073459b0233d16c8ccd6c4/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202025-11-24%20155207.png)


### ✔ Örnek 2 — Kapalı alanda araç tespiti

Model, kapalı otopark ortamındaki araçları doğru şekilde algılamaktadır.

![Detection Result](https://github.com/Amirelahmed/YoloV8_Nesne_Tespiti/blob/aacd920cb6cd4f0349073459b0233d16c8ccd6c4/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202025-11-24%20160339.png)



---

## 🧍 2. İnsan (Person) Tespit Sonuçları  
### ✔ Örnek 1 — Sokak ortamında insan tespiti

Model, açık alandaki yayaları yüksek doğrulukla tespit etmektedir.

![Detection Result](https://github.com/Amirelahmed/YoloV8_Nesne_Tespiti/blob/aacd920cb6cd4f0349073459b0233d16c8ccd6c4/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202025-11-24%20160444.png)

### ✔ Örnek 2 — Kapalı şehir ortamında insan tespiti

![Detection Result](https://github.com/Amirelahmed/YoloV8_Nesne_Tespiti/blob/aacd920cb6cd4f0349073459b0233d16c8ccd6c4/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202025-11-24%20160513.png)

---

## 🚗🧍 3. Karışık Sahne (Araç + İnsan) Tespit Sonuçları  
### ✔ Örnek 1 — Araç ve insanların birlikte bulunduğu sahne

Model hem soldaki oturan kişiyi hem de yoldaki aracı doğru şekilde tespit etmiştir.

![Detection Result](https://github.com/Amirelahmed/YoloV8_Nesne_Tespiti/blob/aacd920cb6cd4f0349073459b0233d16c8ccd6c4/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202025-11-24%20160536.png)

---

🖥️ PyQt5 Masaüstü Arayüz

Bu proje için geliştirilen masaüstü uygulaması, kullanıcıya YOLOv8 nesne tespitini kolay ve görsel olarak anlaşılır bir şekilde sunmaktadır.

✅ Uygulamanın Özellikleri

📤 Görüntü seçme

🤖 YOLOv8 ile nesne tespiti çalıştırma

🖼️ Önce / Sonra görüntülerinin yan yana gösterilmesi

💾 Tespit sonuçlarını kaydetme

▶️ Uygulamayı Çalıştırma

### ▶️ Uygulamayı Çalıştırma

Aşağıdaki tablo uygulamayı çalıştırmak için gerekli adımları göstermektedir:

| Adım | Komut |
|------|-------|
| **Gerekli kütüphaneleri yükleyin** | `pip install pyqt5 ultralytics opencv-python` |
| **Uygulamayı başlatın** | `python gui_app.py` |
| **Not** | `best.pt` dosyası **gui_app.py ile aynı klasörde olmalıdır.** |


### 👨‍💻 Geliştirici Bilgileri

Aşağıdaki tablo proje geliştiricisine ait bilgileri göstermektedir:

| Bilgi | İçerik |
|-------|--------|
| **Ad Soyad** | Amir Elahmed |
| **Ders** | BLG407 – Makine Öğrenmesi |
| **Öğretim Üyesi** | Doç. Dr. Sinan Uğuz |


⭐ Proje Durumu

Bu proje tamamen çalışır durumdadır.

YOLOv8 modeli başarıyla eğitilmiş,

Gerçek görüntüler üzerinde test edilmiş,

PyQt5 masaüstü GUI arayüzü ile entegre edilmiştir.

🏁 Sonuç

Bu repo, YOLOv8 nesne tespiti + PyQt5 GUI entegrasyonunu gösteren tam kapsamlı ve profesyonel bir örnektir.
Hem akademik teslim için hem de kişisel portföy için mükemmel bir projedir.
