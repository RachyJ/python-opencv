import numpy as np
import cv2

image = cv2.imread("D:\\Github\\python-opencv\\images\\coins.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred", image)

thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Mean thresh", thresh) # use thresh_mean as T value; 11 - neighborhood size; -4 (C) to finetune the thresholding

thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("Gaussina thresh", thresh)
cv2.waitKey(0)