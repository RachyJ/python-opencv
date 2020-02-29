import numpy as np
import imutils
import cv2

image = cv2.imread("D:\\Github\\python-opencv\\images\\trex.png")
cv2.imshow("Original", image)
cv2.waitKey(0)

(h, w) = image.shape[:2] # get height and width of the image
center = (w/2, h/2) # which point to rotate around

M = cv2.getRotationMatrix2D(center, 45, 1.0) # rotation matrix
rotated = cv2.warpAffine(image, M, (w, h)) # apply the rotation
cv2. imshow("Rotated by 45 degrees", rotated)
cv2.waitKey(0)

M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 degrees", rotated)
cv2.waitKey(0)

rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180", rotated)
cv2.waitKey(0)