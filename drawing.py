import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype = "uint8")
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0) # wait for a key press; delay 0

red = (0, 0, 255)
cv2.line(canvas, (300,0), (0, 300), red, 3) # 3-thickness
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (10,10), (60,60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1) # solid blue with "-1"
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

canvas = np.zeros((300, 300, 3), dtype = "uint8") # re-initialize canvas to be blank
(centerX, centerY) = (canvas.shape[1] / 2, canvas.shape[0] / 2) # shape[0] - height; shape[1] - width
white = (255, 255, 255)

for r in range(0, 175, 25): # r from 0 to 175, step 25
    cv2.circle(canvas, (int(centerX), int(centerY)), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

for i in range(0, 25): # create 25 circles
    radius = np.random.randint(5, high = 200) # radius [5, 200)
    color = np.random.randint(0, high = 256, size = (3, )).tolist() # return 3 numbers [0, 255]
    pt = np.random.randint(0, high = 300, size = (2,)) # (x,y) at [0, 300) to draw the circle

    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
