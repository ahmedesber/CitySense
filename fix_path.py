import json
import random

# Settings for the path
START_LAT = 41.0965  # Seyrantepe Starting Point
START_LNG = 28.9852
LAT_MOVE = 0.00005   # How much the "car" moves each detection
LNG_MOVE = 0.00008


def fix_coordinates():
    with open('detections.json', 'r') as f:
        data = json.load(f)

    for i, entry in enumerate(data):
        # Simulate movement by adding to the coordinates for each detection
        entry['location']['lat'] = round(START_LAT + (i * LAT_MOVE), 6)
        entry['location']['lng'] = round(START_LNG + (i * LNG_MOVE), 6)

        # Add a tiny bit of "jitter" so the pins aren't in a perfect robot line
        entry['location']['lat'] += random.uniform(-0.00001, 0.00001)
        entry['location']['lng'] += random.uniform(-0.00001, 0.00001)

    with open('detections_path.json', 'w') as f:
        json.dump(data, f, indent=4)

    print(f"✅ Success! Generated {len(data)} unique coordinates.")
    print("Send 'detections_path.json' to Tariq now.")


if __name__ == "__main__":
    fix_coordinates()
