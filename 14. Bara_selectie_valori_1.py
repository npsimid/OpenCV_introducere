import cv2 as cv
import numpy as np

# creaarea unei functi ce va fi apelata cand se va modifica valoarea barei
def actiune(x):
    print(x)

# Crearea unei imagini de culoare neagra
img=np.zeros((300,512,3), np.uint8)

# crearea unui ferestre fara imagnine
cv.namedWindow("image")

# crearea barelor de valori
nume_bara1 = "Albastru" # denumirea barei 1
nume_bara2 = "Verde" # denumirea barei 2
nume_bara3 = "Rosu" # denumirea barei 2
init_val = 0 # setarea valorii initiale
final_val = 255 # setarea valorii finale
cv.createTrackbar(nume_bara1,"image", init_val, final_val, actiune) # creare barei 1
cv.createTrackbar(nume_bara2,"image", init_val, final_val, actiune) # creare barei 2
cv.createTrackbar(nume_bara3,"image", init_val, final_val, actiune) # creare barei 3

# crearea unui comutator
comutator = "0 : OFF\n1 : ON" # denumirea comutatorului
cv.createTrackbar(comutator,"image", 0, 1, actiune) # creare comutatorului

while(1):
    cv.imshow("image", img)
    k = cv.waitKey(1) & 0xFF # se formeaza o variabila ce determina durata de afisare a imaginii
    if k==27:
        break # se inchide imaginea daca se tasteaza Esc (codul tastei este 27)

    # citirea valorilor barelor
    albastru = cv.getTrackbarPos(nume_bara1, "image")
    verde = cv.getTrackbarPos(nume_bara2, "image")
    rosu = cv.getTrackbarPos(nume_bara3, "image")
    comut = cv.getTrackbarPos(comutator, "image")

    # verificarea pozitiei comutatorului
    if comut==0:
        # nu se modifica nimic
        img[:] = 0
    else:
        # setarea culorii ferestrei negre conform valorilor barelor
        img[:] = [albastru,verde,rosu]

cv.destroyAllWindows()