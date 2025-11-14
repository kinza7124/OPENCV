import cv2

image = cv2.imread("free-nature-images.jpg")

blurred = cv2.GaussianBlur(image, (7,7), 3)

cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()