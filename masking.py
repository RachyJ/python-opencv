import numpy as np
import cv2

image = cv2.imread("D:\\Github\\python-opencv\\images\\autumn_impression.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)

mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.imshow("Mask", mask)
cv2.waitKey(0)

(cX, cY) = (image.shape[1]/2, image.shape[0]/2)
cv2.rectangle(mask, (int(cX)- 75, int(cY) - 75), (int(cX) + 75, int(cY) + 75), 255, -1)
cv2.imshow("Mask", mask)
cv2.waitKey(0)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Masked", masked)
cv2.waitKey(0)