import numpy as np
import cv2

image = cv2.imread("D:/Github/python-opencv/images/440px-Lung_X-ray.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert the image to gray

eq = cv2.equalizeHist(image) # perform histogram equalization

cv2.imshow("Hist equalization", np.hstack([image, eq])) # show graycaled image and equalized one
cv2.waitKey(0)