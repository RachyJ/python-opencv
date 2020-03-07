import numpy as np
import cv2

image = cv2.imread("D:\\Github\\python-opencv\\images\\coins.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.waitKey(0)

lap = cv2.Laplacian(image, cv2.CV_64F) # use Laplacian(src, data type for output img) to compute the gradient magnitude 
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)
cv2.waitKey(0)

# Compute the Sobel gradient representation

sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0) # find vertical edge
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1) # find horizontal edge

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel combined", sobelCombined)

cv2.waitKey(0)