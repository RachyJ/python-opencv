# python-opencv

Learning project for image processing knowledge. 

Samples are from book *Practical Python and OpenCV: An Instroductory, Example Driven Guide to Image Processing and Computer Vision* by Adrian Rosebrock.

The original samples in the book are in Python 2 and I convert them to Python 3.

Learning notes:

## Image basics

Pixels are the raw, building blocks of an image. 

Normally, we think of a pixel as the 'color' or the 'intensity' of light that appears in a given place of an image.

Color pixel are normally represented in the RGB color space. 

- [0, 255] , 8-bit unsigned integer
- (255, 255, 2555) : white color
- (0, 0, 0) : black color
- (255, 0, 0): red
- (0, 255, 0): green
- (0, 0, 255): blue


OpenCV represents images as NumPy arrays, in the order of Blue, Green, and Red.

## Image processing

**Image translation**: shift an image along the x or y axis.

```python
def translate(image, x, y):
    M = np.float([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted
```

**Rotation**: rotate an image by some angle.

```python
(h, w) = image.shape[:2]
center = (w/2, h/2) # rotate around the center of the image

M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
```

**Resize**

```python
r = 150.0 / image.shape [1] # ratio of image width to 150
dim = (150, int(image.shape[0] * r))

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

```

**Flipping**

```python
flip_horizon = cv2.flip(image, 1)
flip_vertical = cv2.flip(image, 0)
flip_both = cv2.flip(image, -1)
```

**Cropping**

We can crop image using Numpy array slicing.

cropped = image[30:120, 240:335]

**Image arithmetic: OpenCV vs NumPy**

- Numpy: perform modulus arithmetic and "wrap around"
- OpenCV: ensure pixel values never fall outside the range [0, 255]

**Bitwise operations**

- AND: true only if both pixels are greater than 0
- OR: true if either of the two pixels are > 0
- XOR: true if one of but not both pixels are > 0
- NOT: invert "on" / "off" in an image

**Masking**

Using a mask allows us to focus only on the portions of the image that interest us.

**Splitting and merging channels**

```python
image = cv2.imread("d:/sampleimage.jpg)
(B, G, R) = cv2.split(image)
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

merged = cv2.merge([B, G, R])
```

**Color spaces**

- RGB: an easy start
- HSV (Hue-Saturation-Value)
- Lab

```python
# change color spaces

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
```

## Histograms

A histogram represents the distribution of pixel intensities (color or grayscale) in an image. By simply examining the histogram of an image, you get a general understanding regarding the contrast, brightness, and intensity distribution.

OpenCV method to compute histograms:

```
cv2.calcHist(images, channels, mask, histSize, ranges) # channel for a gray iamge [0]; channels for RGB channels [0, 1, 2]
```

Sample of computing a gray image histogram:

```python
hist = cvs.calcHist([image], [0], None, [256], [0, 256])
```

color histograms:

```python
chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("")
plt.xlable("bins")
plt.ylable("# of pixels")

for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color = color)
    plt.xlim([0, 256])
```

**Histogram equalization**

Histogram equalization improve the contrast of an image by stretching the distribution of pixels. Histogram equalization is applied to grayscale images and is normally useful when enhancing the contrast of medical or satellite images.

```python
cv2.equalizeHist(image)
```

## Smoothing and blurring

Blurring means that each pixel is mixed in with its surrounding pixel intensities. This "mixture" of pixels in a neighborhood becomes the blurred pixel.

Many image processing and computer vision functions, such as thresholding and edge detection, perform better if the image is first smoothed or blurred.

**Averaging**

Use a sliding window (k * k, odd number) as a "convolution kernel" or "kernel" to slid from left to right and from top to bottom. The pixel at the center of the matrix is then set to the avg. of all other pixels surrounding it.

Larger kernel means more blurred image.

```python
cv2.blur(image, (3, 3))
```

**Gaussian**

Gaussian blurring is similar to average blurring but instead of using a weighted mean, where neighborhood pixels that are closer to the central pixel contribute more "weight" to the average.

```python
cv2.GaussianBlur(image, (3, 3), 0) 
```

**Median**

The median blur method is most effective when removing salt-and-pepper noise.

**Bilateral**

Reduce noise while maintaining edges by using two Gaussian distributions.

```python
cv2.bilateralFilter(image, 5, 21, 21)
```

## Thresholding

Binarization of an image. Normally, we use thresholding to focus on objects or areas of particular interest in an image.

```python
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)

(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
```

## Gradients and edge detection

Edge detection embodies mathematical methods to find points in an image where the brightness of pixel intensities changes distinctly.

**Laplacian and sobel**

```python
lap = cv2.Laplacian(grayed, cv2.CV64F)
lap = np.uint8(np.absolute(lap))

# compute Sobel gradient representation to find horizontal and vertial edge-like regions

sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(SobelX))
sobelY = np.uint8(np.absolute(SobelY))
sobelCombined = cv2.bitwise_or(SobelX, SobelY)
```

**Canny edge detection**

The Canny edge detector is a multi-step process that involves 

- blur the image to remove noise
- compute Sobel gradient images in the x and y direction
- suppression of edges
- determine if a pixel is edge-like or not via thresholding

```python
canny = cv2.Canny(GaussianBlurredGray, 30, 150)
```

## Contours

A contours is a curve of points, with no gaps in the curve. Contours are extremely useful for things like shape approximation and analysis.

Basic stpes:

1. Binaraization
2. Blur to remove noises
3. Find edges using edge detection or thresholding
4. Find contours

```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GuassianBlur(gray, (11, 11), 0)
edged = cv2.Canny(blurred, 30, 150)
(conts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
```

