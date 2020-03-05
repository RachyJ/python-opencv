from matplotlib import pyplot as plt
import numpy as np
import cv2

def plot_histogram(image, title, mask = None):
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title (title)
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")

    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256]) # compute a histogram for each channel in the image; channel [0] is for a grayscale image
        plt.plot(hist, color = color)
        plt.xlim([0, 256])
    # plt.show()


image = cv2.imread("D:/Github/python-opencv/images/440px-Lung_X-ray.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)
plot_histogram(image, "Hist for original image")
plt.show()

mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.rectangle(mask, (15, 15), (130, 130), 255, -1)
cv2.imshow("Mask", mask)
cv2.waitKey(0)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Applying the mask", masked)
cv2.waitKey(0)
plot_histogram(image, "Hist for masked image", mask = mask)
plt.show()