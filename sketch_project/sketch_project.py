import cv2

def normal_sketch(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (21, 21), 0)
    sketch = cv2.divide(gray, blur, scale=256)
    return sketch

def enhanced_sketch(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(gray)
    blur = cv2.GaussianBlur(inverted, (25, 25), 0)
    inverted_blur = cv2.bitwise_not(blur)
    sketch = cv2.divide(gray, inverted_blur, scale=256.0)

    # Sharpen for deeper pencil effect
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    sketch = cv2.morphologyEx(sketch, cv2.MORPH_CLOSE, kernel)
    return sketch

def colored_pencil_sketch(image):
    # Convert to grayscale and blur
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 15)

    # Detect edges
    edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)

    # Color smoothing
    color = cv2.bilateralFilter(image, 9, 300, 300)

    # Combine color + edges
    sketch = cv2.bitwise_and(color, color, mask=edges)
    return sketch

image = cv2.imread("Coders_cup.png")

print("\nChoose Sketch Effect:")
print("1. Normal Pencil Sketch")
print("2. Enhanced Pencil Sketch")
print("3. Colored Pencil Sketch")

choice = int(input("\nEnter your choice (1/2/3): "))

if choice == 1:
    result = normal_sketch(image)
    cv2.imshow("Normal Sketch", result)
    cv2.imwrite("Normal_Sketch.png", result)

elif choice == 2:
    result = enhanced_sketch(image)
    cv2.imshow("Enhanced Sketch", result)
    cv2.imwrite("Enhanced_Sketch.png", result)

elif choice == 3:
    result = colored_pencil_sketch(image)
    cv2.imshow("Colored Pencil Sketch", result)
    cv2.imwrite("Colored_Pencil_Sketch.png", result)

else:
    print("\nInvalid Choice! Please run again.\n")
    exit()

cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("\nSketch created successfully and saved!")
