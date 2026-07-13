from ultralytics import YOLO
import os

# Veri setinin bilgisayardaki tam adresi
data_yaml_path = os.path.abspath("veri_seti/data.yaml")

print("YOLOv8 Yapısı sıfırdan kuruluyor...")
# yolov8n doğrudan kütüphanenin içinde gömülü şablon olarak tetiklenebilir
model = YOLO("yolov8n.yaml") 

print(f"Eğitim başlatılıyor! Kullanılan dosya: {data_yaml_path}")

# Eğitimi yerel olarak tetikliyoruz
model.train(
    data=data_yaml_path,  # Bilgisayarındaki yerel data.yaml dosyası
    epochs=10,            # Deneme amaçlı 10 tur
    imgsz=640,            # Görsel boyutu
    device="cpu"          # Bilgisayarın işlemcisi üzerinde eğitsin
)

print("Eğitim tamamlandı! Yeni modeliniz 'runs/detect/train/weights/best.pt' konumuna kaydedildi.")