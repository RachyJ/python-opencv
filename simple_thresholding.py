import numpy as np
import cv2

image = cv2.imread("D:\\Github\\python-opencv\\images\\coins.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0) # apply Gaussian blurring to move some of the high frequency edges
cv2.imshow("image", image)
cv2.waitKey(0)

(T, thresh) = cv2.threshold(blurred,  155, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold binary", thresh)

(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold binary inverse", threshInv)

cv2.imshow("object", cv2.bitwise_and(image, image, mask = threshInv))
cv2.waitKey(0)