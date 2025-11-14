import cv2 

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 

cap = cv2.VideoCapture(0)  
while True: 
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1 , 3)  

# detectMultiScale(image, scaleFactor, minNeighbors)
# balance = 1.1, not too slow, not too fast 
# scans and detects objects at different sizes in the input image.
# minNeighbors = 5, higher value results in less detections but with higher quality  

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
