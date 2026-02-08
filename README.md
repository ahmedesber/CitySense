#🛣️ CitySense: Real-Time Road Monitoring with Edge AI & 5G
CitySense is an end-to-end Smart City infrastructure solution designed to automate road damage detection. Using YOLOv8 at the edge and leveraging 5G low-latency networks, CitySense identifies potholes and cracks in real-time, providing municipalities with an actionable "Damage Heat Map" for proactive maintenance.

🚀 Key Features
Edge AI Detection: Optimized YOLOv8 Nano model for real-time inference on edge devices.

High Accuracy: Validated with a peak 0.87 F1-score on custom training sets.

Field Tested: Successfully validated using real-world mobile footage from Seyrantepe (Kağıthane), Istanbul and Fujairah, UAE.

Automated Reporting: Generates instant detections.json logs with timestamps and confidence scores for every detection.

5G Ready: Designed for high-speed, low-latency data transmission to central management dashboards.

📊 Performance Metrics
The model was trained on the RDD2022 (Road Damage Dataset) and fine-tuned for urban environments.

Model Architecture: YOLOv8n (Nano).

F1-Score: 0.87 (Peak).

Real-World Confidence: Consistent 96% average confidence during field testing.

🛠️ Tech Stack
Language: Python 3.10+.

Frameworks: PyTorch, Ultralytics (YOLOv8).

Computer Vision: OpenCV.

Frontend: React (Dashboard Integration).

💻 Getting Started
1. Installation

Clone the repository and install the required dependencies:
git clone https://github.com/[your-username]/CitySense.git
cd CitySense
pip install -r requirements.txt

2. Running Inference (CLI)

The system includes a professional Command Line Interface (CLI). To run the detection on a video source with custom thresholds:
# Basic usage
python main.py --source data/video.mp4

# Advanced usage with custom weights and confidence
python main.py --source data/fujairah_drive.mp4 --weights models/best.pt --conf 0.5

3. Coordinate Pathing Utility

For static test footage, use our path simulation utility to generate dynamic GPS trails for the dashboard visualization:
python fix_path.py

📂 Data Management Note
Due to GitHub's 100MB file size limit, the full raw image datasets and heavy weight files are hosted on Google Drive.

Weights: Located in the /models directory on GitHub or the shared Drive link.

Datasets: Reach out to the team leads for access to the full RDD2022 augmented set.

📅 Project Roadmap
[x] Initial training on RDD2022 dataset (0.87 F1-score).

[x] Real-world field testing in Seyrantepe, Istanbul.

[x] International environmental testing in Fujairah, UAE.

[x] Development of professional CLI inference tool.

[ ] Integration with Turkcell 5G Simulation Environment.

[ ] Final Submission for Turkcell Tech Leaders Competition (Feb 15).

👥 The Team
Ahmad Esber – Machine Learning Engineer (İstinye University).

Tariq – Systems Integration & Frontend (İstinye University).
