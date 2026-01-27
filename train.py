from ultralytics import YOLO
import os
import yaml


def train_model():
    # 1. Setup Paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Point to the data.yaml inside the datasets folder
    yaml_path = os.path.join(current_dir, 'datasets', 'data.yaml')

    # 2. AUTO-FIX the data.yaml file (Crucial step for Roboflow data)
    # We overwrite the file with correct relative paths so it works on Mac
    data_config = {
        # Absolute path to datasets
        'path': os.path.join(current_dir, 'datasets'),
        'train': 'train/images',
        'val': 'valid/images',
        'test': 'test/images',
        'names': {0: 'pothole'}
    }

    with open(yaml_path, 'w') as f:
        yaml.dump(data_config, f)

    print(f"✅ Configured data at: {yaml_path}")

    # 3. Load Model
    model = YOLO('yolov8n.pt')

    # 4. Train
    print("Starting Training...")
    results = model.train(
        data=yaml_path,
        epochs=25,
        imgsz=640,
        device='mps'  # Apple Silicon GPU
    )


if __name__ == '__main__':
    train_model()
