import numpy as np
import cv2

image = cv2.imread("D:\\Github\\python-opencv\\images\\trex.png")
cv2.imshow("Original", image)
cv2.waitKey(0)

# print(str(np.uint8(200)))

print("max of 255: " + str(cv2.add(np.uint8([200]), np.uint8([100])))) # cv2 range [0, 255]
print("min of 0: " + str(cv2.subtract(np.uint8([50]), np.uint8([100]))))

print("wrap around:" + str(np.uint8([200]) + np.uint8([100]))) # wrap around if out [0, 255]
print("wrap around" + str(np.uint8([50]) - np.uint8([100])))

M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added) # more light: add 100 to each pixel
cv2.waitKey(0)

M = np.ones(image.shape, dtype = "uint8") * 50
added = cv2.subtract(image, M)
cv2.imshow("Subtracted", added) # darker: subtract 50 from each pixel
cv2.waitKey(0)