import cv2 as cv
import numpy as np
imagine = cv.imread("forme_geometrice.jpg")
img_alb_negru = cv.cvtColor(imagine,cv.COLOR_BGR2GRAY)
img = imagine.copy()
_, prag = cv. threshold(img_alb_negru, 240, 255, cv.THRESH_BINARY)

contururi, _ = cv.findContours(prag, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for contur in contururi:
    a = contur

    aprox = cv.approxPolyDP(contur, 0.01* cv.arcLength(contur, True), True) # perfectarea cotururilor prin aproximare
    cv.drawContours(img, [aprox], 0, (0,0,0), 3)

    x=aprox.ravel()[0]
    y=aprox.ravel() [1] - 10
    if len(aprox) == 3:
        cv.putText(img, "Triunghi", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    if len(aprox) == 4:
        x1, y1, w, h = cv.boundingRect(aprox)
        aspect = float(w)/h
        if aspect >=0.95 and aspect<=1.05:
            cv.putText(img, "Patrat", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv.putText(img, "Dreptunghi", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))

    if len(aprox) == 5:
        cv.putText(img, "Pentagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))

    if len(aprox) == 6:
        cv.putText(img, "Hexagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))

    if len(aprox) == 8:
        cv.putText(img, "Optagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))

    if len(aprox) == 10:
        cv.putText(img, "Stea", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))

    if len(aprox) >10:
        cv.putText(img, "Cerc", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
print(a)
print()
print(aprox)
cv.imshow("Imaginea originala", imagine)
cv.imshow("Forme geometrice", img)
cv.waitKey(0)
cv.destroyAllWindows()