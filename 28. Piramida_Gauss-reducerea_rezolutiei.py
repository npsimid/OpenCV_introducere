import cv2 as cv

img = cv.imread("lena.jpg")

# reducerea rezolutie la jumatate
lr1 = cv.pyrDown(img)

# reducerae rezolutie la 1/4
lr2 = cv.pyrDown(lr1)

# reducera rezolutiei la 1/8
lr3 = cv.pyrDown(lr2)

# schimbarea rezolutie de la 1/4 la 1/2 (cu pierdere de calitate)
hr1 = cv.pyrUp(lr2)

cv.imshow("Imagine originala", img)
cv.imshow("Rezolutie 1/2", lr1)
cv.imshow("Rezolutie 1/4", lr2)
cv.imshow("Rezolutie 1/8", lr3)
cv.imshow("Rezolutie 1/2 restabilita", hr1)
cv.waitKey(0)
cv.destroyAllWindows()