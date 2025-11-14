import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() #ret=True/False frame=image

    if not ret:
        print("Could not read frame")
        break

    cv2.imshow("Webcam Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # 113 == 113 True
        print("Quitting....")
        break

cap.release()
cv2.destroyAllWindows() 
