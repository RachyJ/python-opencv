import cv2

image = cv2.imread("D:\\Github\\python-opencv\\images\\trex.png")
cv2.imshow("Original", image)
cv2.waitKey(0)

flipped = cv2.flip(image, 1)
cv2.imshow("Flipped horizontally", flipped)
cv2.waitKey(0)

flipped = cv2.flip(image, 0)
cv2.imshow("Flipped vertically", flipped)
cv2.waitKey(0)

flipped = cv2.flip(image, -1)
cv2.imshow("Flipped horizontally & vertically", flipped)
cv2.waitKey(0)