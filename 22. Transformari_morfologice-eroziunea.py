import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("smarties.png", 0) # doar in regim alb-negru

# crearea mastii cu nivelul de prag - thresholding
_,masca = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV) # pina la 220 devine alb, dupa devine negru

# aplicarea eroziunii pentru reducerea portiunilor albe de pe masca dar si cu cresterea punctelor negre de pe portiuni

kernal = np.ones((3,3), np.uint8) # formarea nucleului (kernal) in patrat de pixeli (toti albi) ce va influenta pixelul central la transformare
iteratii = 2 # numarul de iteratii cu utilizarea nucleului in procesul de transformare

eroziune = cv.erode(masca, kernal, iterations=iteratii) # aplicarea eroziunii


titluri = ["Original", "Masca", "Eroziune"]
imagini = [img, masca, eroziune]

for i in range(len(imagini)):
    plt.subplot(1, 3, i+1) #
    plt.imshow(imagini[i], "gray")
    plt.title(titluri[i])
    plt.xticks([])
    plt.yticks([])

plt.show()