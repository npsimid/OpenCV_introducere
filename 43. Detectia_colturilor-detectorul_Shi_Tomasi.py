import numpy as np
import cv2 as cv

img = cv.imread("forme_geometrice.jpg")

alb_negru = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
nr_max_colturi = 50 #numarul maxim de colturi ce vor fi detectate
nivel_calitate = 0.02 # nivelul minic al calitatii
min_dist = 30 #distanta minima dintre 2 colturi
colturi = cv.goodFeaturesToTrack(alb_negru, nr_max_colturi, nivel_calitate, min_dist)

colturi = np.int0(colturi)

for colt in colturi:
    x, y = colt.ravel()
    cv.circle(img, (x,y), 3, (255,0,255), -1)

cv.imshow("Imagine", img)
cv.waitKey(0)
cv.destroyAllWindows()