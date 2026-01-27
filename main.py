from ultralytics import YOLO
import cv2
import time


def process_walking_video(video_name):
    model = YOLO('runs/detect/train7/weights/best.pt')
    cap = cv2.VideoCapture(video_name)

    print(f"🕵️ Analyzing your walk: {video_name}")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(frame, conf=0.4, verbose=False)

        if len(results[0].boxes) > 0:
            timestamp = time.strftime("%H:%M:%S")
            # We "simulate" the location for the demo
            with open("city_report.txt", "a") as f:
                f.write(
                    f"[{timestamp}] POTHOLE FOUND in Seyrantepe! Check frame.\n")

    cap.release()
    print("📋 Report generated: city_report.txt")


process_walking_video('my_walk.mp4')  # Change this to your video name
