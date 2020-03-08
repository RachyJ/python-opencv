import numpy as np
import cv2

image = cv2.imread("D:\\Github\\python-opencv\\images\\coins.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow("Image", image)

edged = cv2.Canny(blurred, 30, 150) # get the outlines of the coins
cv2.imshow("Edges", edged)

(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # get contours findContours(using a copied img as source, type of contours, how to approximate the contour)

print("I count %d coins in the image" % (len(cnts)))

coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Coins", coins)
cv2.waitKey(0)

for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv2.boundingRect(c)

    print("Coin #%d" % (i+1))
    coin = image[y:y + h, x:x + w]

    mask = np.zeros(image.shape[:2], dtype = "uint8")
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    mask = mask[y: y+h, x:x+w]

    cv2.imshow("Mask coin", cv2.bitwise_and(coin, coin, mask = mask))
    cv2.waitKey(0)