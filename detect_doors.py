"""
Live Webcam Door Detection using YOLOv8
"""

from ultralytics import YOLO
import cv2
import os

# Path to your trained model
MODEL_PATH = r"C:\Users\aashi\Desktop\best.pt"


def main():
    if not os.path.exists(MODEL_PATH):
        print(f"Error: Model not found at {MODEL_PATH}")
        return

    # Load the trained model
    model = YOLO(MODEL_PATH)
    print("Model loaded successfully. Starting live detection...")

    # Open webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Warning: Failed to grab frame from webcam.")
            break

        # Run detection
        results = model(frame, imgsz=640, conf=0.5, device="cpu", verbose=False)

        # Override the class name so it shows "door" instead of the long name
        results[0].names = {0: "door"}
        # =======================================================

        # Draw results on the frame
        annotated_frame = results[0].plot()

        # Show the live detection
        cv2.imshow("Door Detection - Live", annotated_frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Detection stopped.")


if __name__ == "__main__":
    main()
