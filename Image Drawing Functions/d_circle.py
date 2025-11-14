import cv2

image = cv2.imread("python_image.png")

if image is None:
    print("Oops! Your image is not working")

else:
    print("Image loaded successfully!")
    cv2.circle(image, (210,150), 50, (255,0,0), 5)

    cv2.imshow("Drawing Circle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()