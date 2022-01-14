import cv2 as cv
import numpy as np

# creaarea unei functi ce va fi apelata cand se va modifica valoarea barei
def actiune(x):
    print(x)

cv.namedWindow("image")

# crearea barei de valori
cv.createTrackbar("Pozitie","image", 10, 400, actiune) # creare barei

# crearea unui comutator
comutator = "color/alb-negru" # denumirea comutatorului
cv.createTrackbar(comutator,"image", 0, 1, actiune) # creare comutatorului

while(1):
    img = cv.imread("cats.jpg")
    pos = cv.getTrackbarPos("Pozitie", "image") # citirea pozitiei barei
    cv.putText(img, str(pos), (50, 150), cv.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 255), 10) # afisarea valorii barei

    k = cv.waitKey(1) & 0xFF
    if k==27:
        break

    com = cv.getTrackbarPos(comutator, "image")

    if com==0:
        pass
    else:
        # se trece la imagnie alb-negru
        img=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow("image", img)

cv.destroyAllWindows()