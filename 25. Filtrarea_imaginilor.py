import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Eye.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Filtrarea omogena
kernal = np.ones((5,5), np.float32)/25
filtrat =cv.filter2D(img, -1, kernal)

# blurarea imaginii
blurat =cv.blur(img, (5,5))

# Filtarea gaussiana
gauss =cv.GaussianBlur(img, (5,5), 0)

# Filtarea mediana (zgomotul salt-and-pepper)
median = cv.medianBlur(img, 5) # kernal impar

# Filtarea bilaterala (pastreaza marginile)
bilateral=cv.bilateralFilter(img, 9, 75, 75)





titluri = ["Original", "Filtrat", "Blurat", "Gaussian", "Median", "Bilateral"]
imagini = [img, filtrat, blurat,gauss, median, bilateral]

for i in range(len(imagini)):
    plt.subplot(2, 3, i+1) #
    plt.imshow(imagini[i], "gray")
    plt.title(titluri[i])
    plt.xticks([])
    plt.yticks([])

plt.show()