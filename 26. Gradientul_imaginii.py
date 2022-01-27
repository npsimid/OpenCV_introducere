import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("sudoku.png", 0)

# Gradientul Laplace
lap = cv.Laplacian(img, cv.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

# Gradientul SobelX
sobelX = cv.Sobel(img, cv.CV_64F,dx=1, dy=0, ksize=3)
sobelX=np.uint8(np.absolute(sobelX))

# Gradientul SobelY
sobelY = cv.Sobel(img, cv.CV_64F,dx=0, dy=1, ksize=3)
sobelY=np.uint8(np.absolute(sobelY))

# Gradientul Sobel combinat
sobel = cv.bitwise_or(sobelX, sobelY)

titluri = ["Original", "Laplacian", "SobelX", "SobelY", "Sobel Combinat"]
imagini = [img, lap, sobelX, sobelY, sobel]

for i in range(len(imagini)):
    plt.subplot(2, 3, i+1) #
    plt.imshow(imagini[i], "gray")
    plt.title(titluri[i])
    plt.xticks([])
    plt.yticks([])

plt.show()