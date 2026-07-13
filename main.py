import cv2
from ultralytics import YOLO

# Kendi eğittiğin o canavar gibi modeli yüklüyoruz!
model = YOLO("best.pt")

# Kamerayı açıyoruz
cap = cv2.VideoCapture(0)
print("Stealth-Guard AI Başlatıldı. Kapatmak için 'q' tuşuna basın.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Kamera akışı alınamadı.")
        break

    # Kendi modelinle kameradaki görüntüyü analiz et
    results = model(frame, verbose=False)
    annotated_frame = results[0].plot()

    cv2.imshow("Stealth-Guard AI - Canlı Hasar Analizi", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Sistem kapatıldı.")