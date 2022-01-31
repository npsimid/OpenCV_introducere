import numpy as np
import cv2 as cv

img = cv.imread("forme_geometrice.jpg")

alb_negru = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

alb_negru = np.float32(alb_negru)
colturi = cv.cornerHarris(alb_negru, 7, 3, 0.04)

colturi = cv.dilate(colturi,None)

img[colturi>0.01 * colturi.max()] = [0, 0, 255]

cv.imshow("Imagine", img)
cv.waitKey(0)
cv.destroyAllWindows()