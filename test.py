import cv2
import torch
import math
from ultralytics import YOLO

# Object detection model (YOLOv8)
model = YOLO('yolov8n.pt')  # Replace 'yolov8n.pt' with your YOLOv8 model path

def estimate_geolocation(frame, detection, camera_params):
  # Implementation of estimate_geolocation function remains the same

# Server connection details (replace with your actual server information)
server_address = 'your_server_ip'
server_port = 5000

# Main loop
cap = cv2.VideoCapture(0)  # Replace with drone camera access

while True:
  ret, frame = cap.read()

  # Perform object detection with YOLOv8
  results = model(frame)

  # Process detections
  for detection in results.xyxy[0]:
    object_class = detection.names[detection.cls]  # Access class name from results
    confidence = detection.conf
    x_min, y_min, x_max, y_max = detection.xyxy

    object_center = ((x_min + x_max) / 2, (y_min + y_max) / 2)

    # Sample camera parameters (replace with your actual camera parameters)
    camera_params = {
      "focal_length": 35,  # Focal length in mm
      "pixel_width": 1920,  # Image width in pixels
      "pixel_height": 1080,  # Image height in pixels
      "camera_mount_angle": 0,  # Camera mount angle in degrees
      "camera_mount_offset": (0, 0)  # Camera mount offset in mm
    }

    try:
      estimated_lat, estimated_lon, estimated_alt = estimate_geolocation(frame, detection, camera_params)

      # Send estimated geolocation to server
      payload = {
          "object_class": object_class,
          "confidence": confidence,
          "latitude": estimated_lat,
          "longitude": estimated_lon,
          "altitude": estimated_alt
      }
      response = requests.post(f"http://{server_address}:{server_port}/object_detection", json=payload)
      if response.status_code == 200:
          print("Object geolocation sent successfully")
      else:
          print(f"Failed to send object geolocation. Server returned status code: {response.status_code}")
    except Exception as e:
      print(f"Error estimating geolocation: {e}")

  # Display the frame
  cv2.imshow('Frame', frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
