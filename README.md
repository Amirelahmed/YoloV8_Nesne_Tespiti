# 🚀 YOLOv8 Saat & Fare Nesne Tespiti – PyQt5 Masaüstü Uygulaması

Bu proje, BLG407 **Makine Öğrenmesi** dersi kapsamında geliştirilmiş olup YOLOv8 modeli kullanılarak **Saat (Clock)** ve **Fare (Mouse)** nesnelerinin tespit edilmesini amaçlamaktadır.  
Proje kapsamında kullanılan tüm görüntüler **tarafımdan özel olarak çekilmiş**, manual olarak etiketlenmiş ve model bu özgün veri seti üzerinde eğitilmiştir.

---

# 📸 Veri Seti (Tarafımdan Çekilmiştir)

Bu projede kullanılan görüntülerin tamamı **kendi telefonumla çektiğim fotoğraflardan** oluşmaktadır.

| Sınıf | Görüntü Sayısı |
|-------|----------------|
| **Saat (Clock)** | 110 görüntü |
| **Fare (Mouse)** | 110 görüntü |
| **Toplam** | **220 görüntü** |

Tüm görüntüler LabelImg ile YOLO formatında etiketlenmiştir.

### 📌 YOLO Formatı
```python
<class_id> <x_center> <y_center> <width> <height>
```
---

# 🧠 YOLOv8 Model Eğitimi

Model Google Colab üzerinde YOLOv8s tabanlı mimari ile eğitilmiştir.

```python
from ultralytics import YOLO

model = YOLO("yolov8s.pt")
model.train(
    data="/content/dataset/data.yaml",
    epochs=30,
    imgsz=640,
    batch=8
)
```

Eğitim sonucunda elde edilen best.pt dosyası masaüstü uygulamasında kullanılmıştır.

🖥️ PyQt5 Masaüstü Uygulaması

Geliştirilen GUI, kullanıcıya kolay ve anlaşılır bir nesne tespiti deneyimi sunmaktadır.

✔ Uygulama Özellikleri

Her formatta görsel yükleme (JPG, PNG, WEBP vb.)

WEBP dosyalarının otomatik JPEG'e dönüştürülmesi

YOLOv8 ile anında nesne tespiti

Orijinal ve tespit edilmiş görüntünün yan yana gösterilmesi

Sonuç kaydetme özelliği

▶ Çalıştırma
```python
pip install pyqt5 ultralytics opencv-python
python gui.py
```
Model Test Sonuçları

Aşağıdaki örnek sonuçlar, eğitimden sonra modelin gerçek fotoğraflar üzerinde verdiği çıktılardır.
Bu görseller images/ klasörü içinde de bulunmaktadır.

⌚ 1. Saat (Clock) Tespit Sonuçları – 2 Örnek
✔ Örnek 1
![Model1 Loss](https://github.com/Amirelahmed/YoloV8_Nesne_Tespiti/blob/248fd7380760f01e573ed880f668d5ebc0cc953d/images/Saat/saat_1.png)

✔ Örnek 2
![Model1 Loss](https://github.com/Amirelahmed/YoloV8_Nesne_Tespiti/blob/248fd7380760f01e573ed880f668d5ebc0cc953d/images/Saat/saat_2.png)

🖱️ 2. Fare (Mouse) Tespit Sonuçları – 2 Örnek
✔ Örnek 1
![Model1 Loss](https://github.com/Amirelahmed/YoloV8_Nesne_Tespiti/blob/248fd7380760f01e573ed880f668d5ebc0cc953d/images/Saat/saat_1.png)

✔ Örnek 2
![Model1 Loss]
(https://github.com/Amirelahmed/YoloV8_Nesne_Tespiti/blob/248fd7380760f01e573ed880f668d5ebc0cc953d/images/Saat/saat_2.png)

🕒🖱️ 3. Karışık Sahne (Saat + Fare) – 2 Örnek
✔ Örnek 1
![Model1 Loss](https://github.com/Amirelahmed/YoloV8_Nesne_Tespiti/blob/248fd7380760f01e573ed880f668d5ebc0cc953d/images/Birlikte/birlikte_1.png)

✔ Örnek 2
![Model1 Loss](https://github.com/Amirelahmed/YoloV8_Nesne_Tespiti/blob/248fd7380760f01e573ed880f668d5ebc0cc953d/images/Birlikte/birlikte_2.png)

---
# 👤 Hazırlayan
**Amir Elahmed**  
BLG407 – Makine Öğrenmesi  
CNN Görüntü Sınıflandırma Projesi
