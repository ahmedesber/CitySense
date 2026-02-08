import cv2
import json
import argparse
from datetime import datetime
from ultralytics import YOLO

def generate_report(detections, source_name):
    """Generates a professional text summary of the run."""
    total = len(detections)
    if total > 0:
        avg_conf = sum(d['confidence'] for d in detections) / total
    else:
        avg_conf = 0.0

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
Detections saved to detections.json
Map coordinates generated for dashboard.
=========================================
"""
    with open("city_report.txt", "w") as f:
        f.write(report_content)
    print("📄 Professional city_report.txt has been generated.")

def run_detection():
    # --- CLI Setup ---
    parser = argparse.ArgumentParser(description="CitySense Pothole Detection Tool")
    parser.add_argument("--source", type=str, default="test_video.mp4", help="Path to input video file")
    parser.add_argument("--weights", type=str, default="models/best.pt", help="Path to YOLO weights file")
    parser.add_argument("--conf", type=float, default=0.25, help="Confidence threshold (0.0 to 1.0)")
    args = parser.parse_args()

    # --- Load Model ---
    model = YOLO(args.weights)
    print(f"🚀 Starting CitySense Detection on: {args.source}")

    # --- Process Video ---
    results = model.predict(source=args.source, conf=args.conf, save=False, stream=True)
    
    all_detections = []
    LAT, LNG = 41.0965, 28.9852 # Default Seyrantepe Coordinates

    for i, r in enumerate(results):
        for box in r.boxes:
            detection_data = {
                "id": len(all_detections) + 1,
                "confidence": round(float(box.conf[0]), 2),
                "location": {"lat": LAT, "lng": LNG},
                "timestamp": str(i)
            }
            all_detections.append(detection_data)

    # --- Save JSON ---
    with open("detections.json", "w") as f:
        json.dump(all_detections, f, indent=4)
    
    # --- Generate Text Report ---
    generate_report(all_detections, args.source)
    
    print(f"✅ Finished! Found {len(all_detections)} detections.")

if __name__ == "__main__":
    run_detection()
