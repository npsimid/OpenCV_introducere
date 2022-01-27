import cv2 as cv

img = cv.imread("lena.jpg")

# reducerea rezolutie la jumatate
lr1 = cv.pyrDown(img)

# reducerae rezolutie la 1/4
lr2 = cv.pyrDown(lr1)

# reducera rezolutiei la 1/8
lr3 = cv.pyrDown(lr2)

# schimbarea rezolutie de la 1/2 la 1 (cu pierdere de calitate)
hr0 = cv.pyrUp(lr1)

# schimbarea rezolutie de la 1/4 la 1/2 (cu pierdere de calitate)
hr1 = cv.pyrUp(lr2)

# schimbarea rezolutie de la 1/8 la 1/4 (cu pierdere de calitate)
hr2 = cv.pyrUp(lr3)

# determinarea maginilor cu piramida Laplace (imaginea - imaginea restabilita din rezolutie injumatatita)
laplace0 = cv.subtract(img, hr0)
laplace1 = cv.subtract(lr1, hr1)
laplace2 = cv.subtract(lr2, hr2)

cv.imshow("Imagine originala", img)
cv.imshow("Margine rezolutie 1", laplace0)
cv.imshow("Margine rezolutie 1/2", laplace1)
cv.imshow("Margine rezolutie 1/4", laplace2)
cv.waitKey(0)
cv.destroyAllWindows()