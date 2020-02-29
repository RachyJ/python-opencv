import numpy as np
import imutils
import cv2

image = cv2.imread("D:\\Github\\python-opencv\\images\\trex.png")
cv2.imshow("Original", image)
cv2.waitKey(0)

M = np.float32([[1, 0, 25], [0, 1, 50]]) # tx 25 - shift right 25px; ty 50 - shift down 50px
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted down and right", shifted)
cv2.waitKey(0)

M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2. warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted up and left", shifted)
cv2.waitKey(0)

shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted down", shifted)
cv2.waitKey(0)