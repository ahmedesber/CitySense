import cv2
import json
import argparse
from ultralytics import YOLO

def run_detection():
    # --- CLI Setup ---
    # This section allows you to run: python main.py --source "fujairah_test.mp4"
    parser = argparse.ArgumentParser(description="CitySense Pothole Detection Tool")
    parser.add_argument("--source", type=str, default="test_video.mp4", help="Path to input video file")
    parser.add_argument("--weights", type=str, default="models/best.pt", help="Path to YOLO weights file")
    parser.add_argument("--conf", type=float, default=0.25, help="Confidence threshold (0.0 to 1.0)")
    args = parser.parse_args()

    # --- Load Model ---
    # Using your weights that hit the 0.87 F1-score
    model = YOLO(args.weights)
    print(f"🚀 Starting CitySense Detection on: {args.source}")

    # --- Process Video ---
    results = model.predict(source=args.source, conf=args.conf, save=False, stream=True)
    
    all_detections = []
    
    # Static coordinates for the current test (Seyrantepe location)
    # We will update these later with real GPS data from your Fujairah drive
    LAT = 41.0965 
    LNG = 28.9852

    for i, r in enumerate(results):
        for box in r.boxes:
            detection_data = {
                "id": len(all_detections) + 1,
                "confidence": round(float(box.conf[0]), 2),
                "location": {
                    "lat": LAT,
                    "lng": LNG
                },
                "timestamp": str(i) # Frame index as a simple timestamp
            }
            all_detections.append(detection_data)

    # --- Save Results ---
    with open("detections.json", "w") as f:
        json.dump(all_detections, f, indent=4)
    
    print(f"✅ Finished! Found {len(all_detections)} detections.")
    print(f"📁 Data saved to detections.json. Now run 'python fix_path.py' to spread the coordinates.")

if __name__ == "__main__":
    run_detection()
