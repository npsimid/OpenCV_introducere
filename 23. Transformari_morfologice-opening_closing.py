import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("smarties.png", 0) # doar in regim alb-negru

# crearea mastii cu nivelul de prag - thresholding
_,masca = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV) # pina la 220 devine alb, dupa devine negru

kernal = np.ones((3,3), np.uint8)
iteratii = 2

# aplicarea opening adica initial eroziunea apoi delatiunea
opening = cv.morphologyEx(masca, cv.MORPH_OPEN, kernal, iterations=iteratii)

# aplicarea closing adica initial delatiunea apoi eroziunea
closing = cv.morphologyEx(masca, cv.MORPH_CLOSE , kernal, iterations=iteratii)

titluri = ["Original", "Masca", "Opening", "Closing"]
imagini = [img, masca, opening, closing]

for i in range(len(imagini)):
    plt.subplot(2, 2, i+1) #
    plt.imshow(imagini[i], "gray")
    plt.title(titluri[i])
    plt.xticks([])
    plt.yticks([])

plt.show()