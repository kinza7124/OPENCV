import cv2

image = cv2.imread("python_image.png")

if image is None:
    print("Oops! Your image is not working")

else:
    print("Image loaded successfully!")
    cv2.putText(image, "Hello Python Programmers", (50,300),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255,0,0), 2)

    cv2.imshow("Adding text over image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()