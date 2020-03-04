from matplotlib import pyplot as plt
import numpy as np
import cv2

image = cv2.imread("D:/Github/python-opencv/images/ocean.png")
cv2.imshow("Original", image)
cv2.waitKey(0)

chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure() # setup PyPlot figure
plt.title("Flattened color histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")

for (chan, color) in zip(chans, colors): # loop over each channel
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color = color)
    plt.xlim([0, 256])
plt.show()
# cv2.waitKey(0)

fig = plt.figure()

ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32], [0, 256, 0, 256]) # use 32 bins
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D color hist for G and B")
plt.colorbar(p)
plt.show()
# cv2.waitKey(0)

ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D color hist for G and R")
plt.colorbar(p)
plt.show()
# cv2.waitKey(0)

ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D color hist for B and R")
plt.colorbar(p)
plt.show()
print("2d hist shape: %s, with %d values" % hist.shape, hist.flatten().shape[0])

hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print("3D hist shape: %s, with %d values" % (hist.shape, hist.flatten().shape[0]))
plt.show()