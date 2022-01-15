import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("smarties.png", 0) # doar in regim alb-negru

# crearea mastii cu nivelul de prag - thresholding
_,masca = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV) # pina la 220 devine alb, dupa devine negru

# aplicarea delatiunii pentru scoaterea punctelor negre de pe portiunile albe in masca dar si cu largirea portiunilor

kernal = np.ones((3,3), np.uint8) # formarea nucleului (kernal) in patrat de pixeli (toti albi) ce va influenta pixelul central la transformare
iteratii = 2 # numarul de iteratii cu utilizarea nucleului in procesul de transformare

delatiune = cv.dilate(masca, kernal, iterations=iteratii) # aplicarea delatiunii


titluri = ["Original", "Masca", "Delatiune"]
imagini = [img, masca, delatiune]

for i in range(len(imagini)):
    plt.subplot(1, 3, i+1) #
    plt.imshow(imagini[i], "gray")
    plt.title(titluri[i])
    plt.xticks([])
    plt.yticks([])

plt.show()