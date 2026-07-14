# ✈️ Stealth-Guard AI (AESS) - Real-Time Aircraft Damage Detection

Stealth-Guard AI (AESS) is a computer vision project powered by deep learning, designed to detect structural damages (such as cracks, corrosion, etc.) on aircraft and UAV surfaces in real time. 

This project utilizes the state-of-the-art YOLO object detection architecture, trained locally on custom datasets and optimized to run seamlessly via a live webcam or camera feed.

---

## 🚀 Key Features
* **Real-Time Inference:** High-speed object detection from live camera streams with millisecond-level latency.
* **Custom-Trained Model:** Leverages a custom-trained weights file (`best.pt`) tailored specifically for structural aviation defects.
* **Lightweight & Efficient:** Designed to run smoothly even on CPU-only environments, ensuring accessibility across various hardware setups.

---

## 📊 Training Performance & Metrics

The model was trained locally using a custom dataset. The training logs, loss curves, and evaluation metrics indicating the model's accuracy are detailed below:

| Model Version | Architecture | Input Image Size |
| :--- | :--- | :--- |
| **Stealth-Guard v1.0** | YOLOv8n | 640x640 |

### Training Results (Loss & Accuracy)


---

## 🛠️ Installation & Quick Start

Follow these steps to set up and run the project on your local machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/Aessteam/Aess.git](https://github.com/Aessteam/Aess.git)
cd Aess
