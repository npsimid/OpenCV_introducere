import numpy as np
import cv2 as cv

img = cv.imread("forme_geometrice.jpg")
img_copie = img.copy()


alb_negru = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
alb = cv.medianBlur(alb_negru, 5) # filtrarea imagine
cercuri = cv.HoughCircles(alb_negru, cv.HOUGH_GRADIENT, 1, 20,
                          param1=50, param2=30, minRadius=0, maxRadius=0) # detectia cercurilor (intoarece lista cu coordonate centru si raza)
print(cercuri)
cercuri_detectate = np.uint16(np.around(cercuri)) # tranformarea datelor cercurilor din float in int
print(cercuri_detectate)

for x,y,r in cercuri_detectate[0, :]:
    cv.circle(img_copie, (x,y), r, (0,255,0), 3)  # desenarea  cercului
    cv.circle(img_copie, (x, y), 2, (0, 255, 255), 3) # desenarea centrului
cv.imshow("Rezultat", img_copie)
cv.waitKey(0)
cv.destroyAllWindows()