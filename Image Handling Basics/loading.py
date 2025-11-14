import cv2

image = cv2.imread("python_image.png")

if image is None:
    print("Error: Image not found")
else:
    print("Image loaded successfully")