import cv2 as cv
import  matplotlib.pyplot as plt

img = cv.imread("gradient.png", 0)

# diferite tipuri de thresholding
_,pr1=cv.threshold(img, 127, 255, cv.THRESH_BINARY)
_,pr2=cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
_,pr3=cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_,pr4=cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_,pr5=cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

titluri = ["Original", "BINARY", "BINARY_INV", "TRUNC", "TOZERO", "TOZERO_INV"] # lista titlurilor tuturor imaginilor
imagini = [img, pr1, pr2, pr3, pr4, pr5] # lista tutror imaginilor

for i in range(6):
    plt.subplot(2, 3, i+1) # crearea ordinii si numarului de subfiguri
    plt.imshow(imagini[i], "gray") # fixarea imaginilor in fiecare subgfiguri
    plt.title(titluri[i]) # fixarea titlului fiecarei subfiguri
    plt.xticks([])
    plt.yticks([])

plt.show()
