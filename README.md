# 🛣️ CitySense: Real-Time Road Monitoring with Edge AI & 5G

**CitySense** is an end-to-end Smart City infrastructure solution designed to automate road damage detection. Using **YOLOv8** at the edge and leveraging **5G low-latency networks**, CitySense identifies potholes and cracks in real-time, providing municipalities with an actionable "Damage Heat Map" for proactive maintenance.

## 🚀 Key Features

* **Edge AI Detection:** Optimized **YOLOv8 Nano** model for real-time inference on edge devices.
* **High Accuracy:** Validated with a peak **0.87 F1-score** on custom training sets.
* **Field Tested:** Successfully validated using real-world mobile footage from **Seyrantepe (Kağıthane), Istanbul**.
* **Automated Reporting:** Generates instant `city_report.txt` logs with timestamps and confidence scores for every detection.
* **5G Ready:** Designed for high-speed, low-latency data transmission to central management dashboards.

## 📊 Performance Metrics

The model was trained on the **RDD2022 (Road Damage Dataset)** and fine-tuned for urban environments.

* **Model Architecture:** YOLOv8n (Nano)
* **F1-Score:** 0.87 (Peak)
* **Inference Speed:** Optimized for real-time mobile deployment

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Frameworks:** PyTorch, Ultralytics (YOLOv8)
* **Computer Vision:** OpenCV
* **Data Analysis:** Pandas, NumPy

## 💻 Getting Started

### 1. Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/[your-username]/CitySense.git
cd CitySense
pip install -r requirements.txt

```

### 2. Running Inference

To run the detection system on a video source:

```bash
python main.py --source path/to/video.mp4

```

## 📅 Project Roadmap

* [x] Initial training on RDD2022 dataset (0.87 F1-score)
* [x] Real-world field testing in Seyrantepe
* [ ] Development of React-based management dashboard
* [ ] Integration with Turkcell 5G Simulation Environment
* [ ] Final Submission for Turkcell Tech Leaders Competition (Feb 15)

## 👥 The Team

* **Ahmad Esber** – Machine Learning Engineer (İstinye University)
* **Tarik** – Systems Integration & Backend (İstinye University, 3rd Year)
