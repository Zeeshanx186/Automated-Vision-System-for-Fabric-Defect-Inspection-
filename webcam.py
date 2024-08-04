from ultralytics import YOLO
import cv2
import math
import time

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

model = YOLO("best_1.pt")
classNames = ["defective"]

# Initialize variables for FPS calculation
start_time = time.time()
frame_count = 0

while True:
    success, img = cap.read()
    
    if not success:
        print("Failed to capture frame from webcam")
        break
    
    frame_count += 1
    
    # Doing detections using YOLOv8 frame by frame
    results = model(img, stream=True)
    
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])
            class_name = classNames[cls]
            label = f'{class_name}{conf}'
            t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
            c2 = x1 + t_size[0], y1 - t_size[1] - 3
            cv2.rectangle(img, (x1, y1), c2, [255, 0, 255], -1, cv2.LINE_AA)  # filled
            cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)
    
    out.write(img)
    cv2.imshow("Image", img)
    
    # Calculate and display FPS every second
    if time.time() - start_time >= 1:
        fps = frame_count / (time.time() - start_time)
        print(f"FPS: {fps:.2f}")
        start_time = time.time()
        frame_count = 0
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()
