import cv2 as cv

img =cv.imread("cats.jpg")

# extragere canale de culori
albastru, verde, rosu = cv.split(img)

# combinarea canale culoru
img_rezultat = cv.merge((albastru, verde, rosu))

cv.imshow('imagine', img)
cv.imshow('albastru', albastru)
cv.imshow('verde', verde)
cv.imshow('rosu', rosu)
cv.imshow('imagine obtinuta', img_rezultat)

cv.waitKey(0)
cv.destroyAllWindows()