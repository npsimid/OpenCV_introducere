import cv2 as cv

img =cv.imread("cats.jpg")

# determinarea dimensiunilor imaginii
dim=img.shape
print(dim)

# determinarea numarului de pixeli
num_pix=img.size
print(num_pix)

# determinare tip de date pt fiecare pixel
data_tip = img.dtype
print(data_tip)

# extragere canale de culori
albastru, verde, rosu = cv.split(img)

cv.imshow('imagine', img)
cv.imshow('albastru', albastru)
cv.imshow('verde', verde)
cv.imshow('rosu', rosu)
cv.waitKey(0)
cv.destroyAllWindows()