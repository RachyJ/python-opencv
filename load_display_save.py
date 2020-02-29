import argparse
import cv2

print (cv2.__version__)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to the image")
args = vars(ap.parse_args())


# image = cv2.imread(args["image"])
image = cv2.imread("D:\\Github\\python-opencv\\images\\trex.png")
print ("width: %d pixels" % (image.shape[1]))
print ("height: %d pixels" % (image.shape[0]))
print ("channels: %d" % (image.shape[2]))

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.imwrite("newimage.jpg", image)