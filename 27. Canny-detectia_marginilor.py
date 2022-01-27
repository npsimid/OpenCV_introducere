import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("cats.jpg", 0)

val_prag_1 = 100 # valoarae de prag 1
val_prag_2 = 200 # valoarea de prag 2

canny = cv.Canny(img, val_prag_1, val_prag_2)

titluri = ["Original", "Canny"]
imagini = [img, canny]

for i in range(len(imagini)):
    plt.subplot(1, 2, i+1) #
    plt.imshow(imagini[i], "gray")
    plt.title(titluri[i])
    plt.xticks([])
    plt.yticks([])

plt.show()