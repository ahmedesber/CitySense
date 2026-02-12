
---

# 🛣️ CitySense: Real-Time Road Monitoring with Edge AI & 5G

**CitySense** is a production-grade Smart City infrastructure solution designed to automate road damage detection. By deploying **YOLOv8** at the edge and leveraging **5G low-latency networks**, CitySense identifies potholes and cracks in real-time, providing municipalities with an actionable "Damage Heat Map" for proactive maintenance.

> 🌐 **Live Dashboard:** [city-sense-one.vercel.app][[(https://www.google.com/search?q=https://city-sense-one.vercel.app)](https://city-sense-lac.vercel.app)](https://city-sense-lac.vercel.app)
> **Field Validation:** Real-time inference results from Seyrantepe (Istanbul, TR) and Fujairah (UAE).

---

## 🚀 Key Features

### 📡 5G-Enabled Edge Intelligence

Optimized for high-speed mobile environments, CitySense utilizes **5G Ultra-Reliable Low-Latency Communication (URLLC)**. This reduces the "Detection-to-Dashboard" latency to **sub-20ms**, enabling near-instantaneous reporting from moving municipal vehicles.

### 🧠 Edge AI Detection

Utilizes a fine-tuned **YOLOv8 Nano** model, specifically chosen for its high throughput and low computational footprint on edge hardware (e.g., mobile devices and IoT gateways).

### 🌍 Multi-Environment Validation

Successfully validated across diverse urban topographies:

* **Istanbul, Turkey:** High-density urban testing in Seyrantepe (Kağıthane).
* **Fujairah, UAE:** High-temperature, high-contrast environment testing.

---

## 🏗️ System Architecture

```text
[Mobile/Edge Camera] --(YOLOv8 Inference)--> [5G Edge Node] --(URLLC)--> [Cloud Backend] --> [React Dashboard]

```

---

## 📈 Performance Metrics

The model was trained on the **RDD2022 (Road Damage Dataset)** and fine-tuned for diverse urban asphalt conditions.

### Technical Validation

* **F1-Score:** 0.87 (Validated Peak)
* **Average Confidence:** 96%
* **Inference Speed:** ~12ms per frame (Optimized for M1/Edge hardware)

---

## 🛠️ Tech Stack

| Layer | Technology |
| --- | --- |
| **Language** | Python 3.10+, TypeScript |
| **AI Framework** | YOLOv8 (Ultralytics), PyTorch |
| **Frontend** | Next.js 16, React, Mapbox GL |
| **Deployment** | Vercel (CI/CD), GitHub |
| **Network** | Optimized for Turkcell 5G URLLC Simulation |

---

## 👥 The Engineer

* **Ahmad Esber** – Lead AI & Full-Stack Engineer (İstinye University)
* *Solo Developer responsible for the full-cycle pipeline: Model training, Data engineering, and Cloud architecture.*



---

### 📜 Acknowledgments

Special thanks to the creators of the **RDD2022 (Road Damage Dataset)** for providing the foundational training data.

---
