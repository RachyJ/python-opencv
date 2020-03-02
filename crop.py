import numpy as np
import cv2

image = cv2.imread("D:\\Github\\python-opencv\\images\\trex.png")
cv2.imshow("Original", image)
cv2.waitKey(0)

cropped = image[30:120, 240:355]
cv2.imshow("T-rex face", cropped)
cv2.waitKey(0)