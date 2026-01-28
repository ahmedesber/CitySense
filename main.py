from ultralytics import YOLO
import cv2
import time
import json  # Essential for the data bridge


def process_walking_video(video_name):
    # Load the model from your new clean path
    model = YOLO('models/best.pt')
    cap = cv2.VideoCapture(video_name)

    # Check if video actually opened
    if not cap.isOpened():
        print("❌ Error: Could not find the video file!")
        return

    all_detections = []
    print(f"🕵️ Analyzing: {video_name}")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Use a slightly lower confidence (0.25) to ensure we get data
        results = model.predict(frame, conf=0.25, verbose=False)

        for box in results[0].boxes:
            timestamp = time.strftime("%H:%M:%S")

            # Create the structured data for the dashboard
            detection_entry = {
                "type": "pothole",
                "confidence": round(float(box.conf[0]), 2),
                "timestamp": timestamp,
                # Seyrantepe placeholder
                "location": {"lat": 41.0965, "lng": 28.9852}
            }
            all_detections.append(detection_entry)

            # Save the JSON file immediately so it doesn't stay empty []
            with open("detections.json", "w") as f:
                json.dump(all_detections, f, indent=4)

    cap.release()
    print("📋 Success! Check 'detections.json' for the data.")


process_walking_video('my_walk.mp4')
