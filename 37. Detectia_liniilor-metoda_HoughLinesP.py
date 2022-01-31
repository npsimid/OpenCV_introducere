import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png')
alb_negru = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # tranformarea in alb-negru
margini = cv.Canny(alb_negru, 50, 200, apertureSize=3) # detectarea marginilor
lung_min = 100 # lungimea minima a liniei
dist_min =10 # distatanta minima dintre linii pentru a fi tratate ca 2 linii
linii  = cv.HoughLinesP(margini, 1, np.pi/180, 100, lung_min, dist_min) # determinarea coodonatelor a 2 puncte pentru fiecare linie

for linie in linii:
    x1, y1, x2, y2 = linie[0]  # citirea coodonatelor pentru fiecare linie

    cv.line(img, (x1,y1), (x2, y2), (0, 255, 255), 2) #desenarea liniei finite

cv.imshow("imagine", img)
cv.imshow("margini", margini)
k=cv.waitKey(0)
cv.destroyAllWindows()