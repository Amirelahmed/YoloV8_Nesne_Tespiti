# 🚀 YOLOv8 Car & Person Detection – PyQt5 GUI

Bu proje, YOLOv8 derin öğrenme modeli kullanılarak **Araç (Car)** ve **İnsan (Person)** tespiti yapan gelişmiş bir bilgisayarlı görü uygulamasıdır.  
Model Google Colab üzerinde eğitilmiş ve sonuçlar PyQt5 masaüstü uygulaması ile sunulmuştur.

---

# 📂 Proje Yapısı

Aşağıdaki tablo, repoda şu anda bulunan gerçek dosyaları göstermektedir:

| Klasör / Dosya | Açıklama |
|----------------|----------|
| `gui_app.py`   | PyQt5 masaüstü uygulaması (GUI) |
| `best.pt`      | Eğitilmiş YOLOv8 model dosyası |
| `README.md`    | Proje açıklama dosyası |
| `Ekran görüntüsü ... .png` | Model test sonuç görüntüleri (5 adet) |


---

# 📚 Veri Seti Açıklaması

Bu projede iki sınıftan oluşan özel bir görüntü veri seti kullanılmıştır:

Car (Araba): 100 görüntü

Person (İnsan): 100 görüntü
📌 Toplam: 200 görüntü

Tüm görüntüler YOLOv8 formatına uygun olarak LabelImg aracı ile elle etiketlenmiştir.
Her görüntüye karşılık bir .txt dosyası oluşturulmuş ve bounding box bilgileri aşağıdaki

## YOLO formatında kaydedilmiştir:
```python
<class_id> <x_center> <y_center> <width> <height>
```
## Örnek bir etiket satırı:
```python
0 0.558565 0.535741 0.812500 0.327037
```
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


🏁 Sonuç

Bu repo, YOLOv8 ile nesne tespiti ve PyQt5 masaüstü kullanıcı arayüzünün birleşimini gösteren tam kapsamlı ve profesyonel bir projedir.

✔ Model başarıyla eğitilmiş
✔ Gerçek görüntüler üzerinde test edilmiştir
✔ PyQt5 arayüzü ile tamamen çalışır durumdadır

Bu proje hem akademik teslim gereksinimlerini eksiksiz karşılar hem de portföy için oldukça güçlü bir örnektir.
