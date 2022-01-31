import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png')
alb_negru = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # tranformarea in alb-negru
margini = cv.Canny(alb_negru, 50, 150, apertureSize=3) # detectarea marginilor
linii  = cv.HoughLines(margini, 1, np.pi/180, 200) # determinarea parametrilor rho si theta a tranforamtei Hough pentru toate liniile

for linie in linii:
    rho, theta = linie[0]  # citirea parametrilor rho si theta pentru fiecare linie
    # trecera parametrilor rho si theta din coor. polarea in x si y in coor. cateziene
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    # deteminarea coodonatelor primului punct
    x1 = int(x0+1000*(-b))
    y1 = int(y0+1000*a)
    # deteminarea coodonatelor celui de al doilea punct
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * a)
    #desenarea liniei infinite
    cv.line(img, (x1,y1), (x2, y2), (0, 0, 255), 2)

cv.imshow("imagine", img)
cv.imshow("margini", margini)
k=cv.waitKey(0)
cv.destroyAllWindows()