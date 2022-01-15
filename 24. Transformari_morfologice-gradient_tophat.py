import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("smarties.png", 0) # doar in regim alb-negru

# crearea mastii cu nivelul de prag - thresholding
_,masca = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV) # pina la 220 devine alb, dupa devine negru

kernal = np.ones((3,3), np.uint8)
iteratii = 2

# aplicarea gradient  - diferenta dintre delatiune si eroziune
grad = cv.morphologyEx(masca, cv.MORPH_GRADIENT, kernal, iterations=iteratii)

# aplicarea tophat - diferenta dintre masca si transformarea opening
top = cv.morphologyEx(masca, cv.MORPH_TOPHAT , kernal, iterations=iteratii)

titluri = ["Original", "Masca", "Gradient", "Tophat"]
imagini = [img, masca, grad, top]

for i in range(len(imagini)):
    plt.subplot(2, 2, i+1) #
    plt.imshow(imagini[i], "gray")
    plt.title(titluri[i])
    plt.xticks([])
    plt.yticks([])

plt.show()