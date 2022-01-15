import cv2 as cv
import matplotlib.pyplot as plt

img =cv.imread("lena.jpg")

# afisarea imaginii in openCV
cv.imshow('imagine', img)

# afisarea imaginii in format BGR in matplotlib
# plt.imshow(img)
# plt.show()

# modificarea imaginii in format RGB si afisarea in matplotlib
img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img2)
# plt.xticks([]), plt.yticks([]) # acunde scara de pe axele x si y
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()