'''from ultralytics import YOLO
#from ultralytics.yolo.v8.detect.predict import DetectionPredictor

import cv2

model = YOLO("yolov8s.pt")

results = model.predict(source="0", show = True)
print(results)

from ultralytics import YOLO
import cv2

# Load the trained YOLO model
model = YOLO("yolov8s.pt")  # Replace with your custom model path if needed

# Initialize webcam (0 for built-in camera, or use 1, 2 for external cameras)
cap = cv2.VideoCapture(0)

# Check if camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Run YOLO prediction
    results = model.predict(frame, conf=0.3, imgsz=640)

    # Render the predictions on the frame
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("YOLOv8 - Live Detection", annotated_frame)
    cv2.waitKey(1)  # Add this line to refresh window properly

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
'''
from ultralytics import YOLO
import cv2
import pyttsx3  # Import TTS module

# Initialize Text-to-Speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Adjust speech speed

# Load the trained YOLO model
model = YOLO("yolov8s.pt")  # Replace with your custom model path if needed

# Initialize webcam (0 for built-in camera, or use 1, 2 for external cameras)
cap = cv2.VideoCapture(0)

# Check if camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Run YOLO prediction
    results = model.predict(frame, conf=0.3, imgsz=640)

    # Render the predictions on the frame
    annotated_frame = results[0].plot()

    # Extract detected object names
    detected_objects = set()
    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])  # Get class index
            label = model.names[cls]  # Get class name
            detected_objects.add(label)

    # Convert detected objects to speech
    if detected_objects:
        objects_text = ", ".join(detected_objects)
        print("Detected:", objects_text)
        engine.say(f"Detected {objects_text}")
        engine.runAndWait()

    # Display the annotated frame
    cv2.imshow("YOLOv8 - Live Detection", annotated_frame)
    cv2.waitKey(1)  # Ensure proper window refresh

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
