import cv2
import json
import argparse
import os
from datetime import datetime
from ultralytics import YOLO

def generate_report(detections, source_name):
    """Generates a professional text summary of the run."""
    total = len(detections)
    # Calculate average confidence for the report
    avg_conf = sum(d['confidence'] for d in detections) / total if total > 0 else 0.0

    report_content = f"""
=========================================
      CITYSENSE: ROAD DAMAGE REPORT
=========================================
Date/Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Source: {source_name}
-----------------------------------------
STATISTICS:
- Total Potholes Detected: {total}
- Average Confidence: {avg_conf:.2%}
- Status: {'Action Required' if total > 5 else 'Normal'}

LOGS:
- Data synced to root: detections.json
- Data synced to frontend: citysense-dash/data/detections.json
- Visual Overlay saved to: runs/detect/
=========================================
"""
    with open("city_report.txt", "w") as f:
        f.write(report_content)
    print("📄 Professional city_report.txt generated.")

def run_detection():
    # --- CLI Setup ---
    parser = argparse.ArgumentParser(description="CitySense Pothole Detection Tool")
    parser.add_argument("--source", type=str, default="my_walk.mp4", help="Path to input video")
    parser.add_argument("--weights", type=str, default="models/best.pt", help="Path to weights")
    parser.add_argument("--conf", type=float, default=0.25, help="Confidence threshold")
    args = parser.parse_args()

    # --- Path Management ---
    # Ensures the frontend sees the data for the Turkcell judges
    DASHBOARD_DATA_PATH = os.path.join("citysense-dash", "data", "detections.json")
    ROOT_DATA_PATH = "detections.json"

    # --- Load Model ---
    # Loading your custom YOLOv8 model
    model = YOLO(args.weights)
    print(f"🚀 CitySense AI Active. Source: {args.source}")

    # --- Process Video ---
    # UPDATED: save=True now creates a video with red boxes for your presentation
    results = model.predict(
        source=args.source, 
        conf=args.conf, 
        save=True, 
        stream=True
    )

    all_detections = []
    # Hardcoded: Fujairah, UAE Coordinates for your field testing
    LAT, LNG = 25.1288, 56.3265

    for i, r in enumerate(results):
        for box in r.boxes:
            detection_data = {
                "id": len(all_detections) + 1,
                "confidence": round(float(box.conf[0]), 2),
                "location": {"lat": LAT, "lng": LNG},
                "timestamp": str(i)
            }
            all_detections.append(detection_data)

    # --- Dual-Path Save (The "Bridge") ---
    # This keeps your backend and frontend in sync solo
    for path in [ROOT_DATA_PATH, DASHBOARD_DATA_PATH]:
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
            with open(path, "w") as f:
                json.dump(all_detections, f, indent=4)
        except Exception as e:
            print(f"⚠️ Warning: Could not sync to {path}: {e}")

    generate_report(all_detections, args.source)
    print(f"✅ Finished! Found {len(all_detections)} detections.")
    print(f"📂 Check 'runs/detect/' for your visualized output video.")

if __name__ == "__main__":
    run_detection()