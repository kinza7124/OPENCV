# OpenCV Projects Collection  
A hands-on collection of OpenCV projects written in Python, covering image sketching, shape & contour detection, face detection, drawing functions, and gesture-based volume control.

---

## 🚀 Projects Overview

### 🔺 Contour & Shape Detection  
Detects geometric shapes (circles, rectangles, triangles, etc.) and their contours using OpenCV methods like `findContours` and `approxPolyDP`.  
Useful for learning basic shape recognition workflows.

### 😀 Face, Eyes and Smile Detection
Real-time face detection project using OpenCV. Capture video input, detect faces and display bounding boxes. Ideal for basic computer-vision applications.

### ✋ Gesture Volume Control  
Control your computer’s volume using hand gestures! Tracks landmarks of your hand and maps thumb-index finger distance to system volume. Integrates hand-tracking and audio control libraries. 

### 🎨 Image Drawing Functions  
A collection of scripts that demonstrate drawing on images: lines, circles, shapes and text overlays. 

### 🖼️ Sketch Project  
Convert an image into a pencil-sketch style. Steps include grayscale conversion, Gaussian blur, inversion, and dodge blending to achieve the sketch effect.

---

## 🛠️ Technologies Used  
- Python  
- OpenCV  
- NumPy  
- For gesture project: MediaPipe (hand tracking) + audio control library  
- Jupyter Notebook / scripts

---

## ▶️ How to Run  
1. Clone the repository:
```bash
git clone https://github.com/kinza7124/OPENCV.git
cd OPENCV
```

2. Install dependencies:
   
```
pip install opencv-python numpy
```

For gesture volume control also install (depending on your OS):
```
pip install mediapipe pycaw
```

3. Choose a project folder and run the script:
```
python "Contour_&_Shape Detection/contour.py"
```
  
