Yes, exactly like that. This version is sharp, technical, and highlights the **0.87 F1-score** and **96% confidence** that prove your model's performance. It also clearly explains the **Google Drive** situation, which should help avoid any more "missing data" arguments with Tariq.

Here is the final raw Markdown for you to copy and paste directly into your **README.md** file:

---

```markdown
# 🛣️ CitySense: Real-Time Road Monitoring with Edge AI & 5G

**CitySense** is an end-to-end Smart City infrastructure solution designed to automate road damage detection. Using **YOLOv8** at the edge and leveraging **5G low-latency networks**, CitySense identifies potholes and cracks in real-time, providing municipalities with an actionable "Damage Heat Map" for proactive maintenance.

## 🚀 Key Features

* **Edge AI Detection:** Optimized **YOLOv8 Nano** model for real-time inference on edge devices.
* **High Accuracy:** Validated with a peak **0.87 F1-score** on custom training sets.
* **Global Field Testing:** Successfully validated using real-world mobile footage from both **Seyrantepe (Kağıthane), Istanbul** and **Fujairah, UAE**.
* **Automated Reporting:** Generates instant `detections.json` logs with timestamps and confidence scores for every detection.
* **5G Ready:** Designed for high-speed, low-latency data transmission to central management dashboards.

## 📊 Performance Metrics

The model was trained on the **RDD2022 (Road Damage Dataset)** and fine-tuned for urban environments.

* **Model Architecture:** YOLOv8n (Nano).
* **F1-Score:** 0.87 (Peak).
* **Real-World Reliability:** Consistent **96% average confidence** during field validation tests.



## 🛠️ Tech Stack

* **Language:** Python 3.10+.
* **Frameworks:** PyTorch, Ultralytics (YOLOv8).
* **Computer Vision:** OpenCV.
* **Frontend:** React-based management dashboard.

## 💻 Getting Started

### 1. Installation

Clone the repository and install the required dependencies:

```bash
git clone [https://github.com/](https://github.com/)[your-username]/CitySense.git
cd CitySense
pip install -r requirements.txt

```

### 2. Running Inference (CLI)

The system features a professional Command Line Interface (CLI). You can run the detection on any video source with custom thresholds directly from the terminal:

```bash
# Basic usage
python main.py --source data/test_video.mp4

# Advanced usage with custom weights and confidence threshold
python main.py --source data/fujairah_drive.mp4 --weights models/best.pt --conf 0.5

```

### 3. Coordinate Pathing Utility

For static test footage, use our path simulation utility to generate dynamic GPS trails for the dashboard visualization:

```bash
python fix_path.py

```

## 📂 Data Management Note

Due to GitHub's **100MB file size limit**, the full raw image datasets and weight files are hosted on **Google Drive**.

* **Weights:** Located in the `/models` directory on GitHub or the shared Drive link.
* **Datasets:** For access to the full RDD2022 augmented set, please use the provided Google Drive link.

## 📅 Project Roadmap

* [x] Initial training on RDD2022 dataset (**0.87 F1-score**).
* [x] Real-world field testing in **Seyrantepe, Istanbul**.
* [x] International environmental testing in **Fujairah, UAE**.
* [x] Development of professional CLI inference tool.
* [ ] Integration with Turkcell 5G Simulation Environment.
* [ ] Final Submission for Turkcell Tech Leaders Competition (Feb 15).

## 👥 The Team

* **Ahmad Esber** – Machine Learning Engineer (İstinye University).
* **Tariq** – Systems Integration & Frontend (İstinye University).

```

---
