import cv2 as cv
import numpy as np

def actiune(x):
    print(cul_inf)

cap = cv.VideoCapture(0) # se va folosi doar cand se va utiliza detectia obiectelor intr-un video
cv.namedWindow("Selectie_culoare")

# crearea barelor de selectie a limitei de jos a culorii
cv.createTrackbar("nua_inf","Selectie_culoare", 0, 255, actiune) # selectie nuanta
cv.createTrackbar("sat_inf","Selectie_culoare", 0, 255, actiune) # selectie saturatie
cv.createTrackbar("lum_inf","Selectie_culoare", 0, 255, actiune) # selectie luminozitate

# crearea barelor de selectie a limitei de sus a culorii
cv.createTrackbar("nua_sup","Selectie_culoare", 255, 255, actiune) # selectie nuanta
cv.createTrackbar("sat_sup","Selectie_culoare", 255, 255, actiune) # selectie saturatie
cv.createTrackbar("lum_sup","Selectie_culoare", 255, 255, actiune) # selectie luminozitate

while(1):
    # img = cv.imread("smarties.png") # se va folosi doar cand se va utiliza detectia pe imagine
    _, img = cap.read() # se va folosi doar cand se va utiliza detectia obiectelor intr-un video

    # conversia imagini din format BGR in HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # citirea limitelor inferioare a culorii dorite
    nua_inf = cv.getTrackbarPos("nua_inf", "Selectie_culoare")
    sat_inf = cv.getTrackbarPos("sat_inf", "Selectie_culoare")
    lum_inf = cv.getTrackbarPos("lum_inf", "Selectie_culoare")

    # citirea limitelor superioare a culorii dorite
    nua_sup = cv.getTrackbarPos("nua_sup", "Selectie_culoare")
    sat_sup = cv.getTrackbarPos("sat_sup", "Selectie_culoare")
    lum_sup = cv.getTrackbarPos("lum_sup", "Selectie_culoare")

    # Determinarea culorilor superioar si inferioare
    cul_inf = np.array([nua_inf, sat_inf, lum_inf]) # culoarea inferioara
    cul_sup = np.array([nua_sup, sat_sup, lum_sup]) # culoarea superioara

    # crearea mastii (0 - culoarea este in afara diapazonului, 255 - cloarea in diapazon)
    mask = cv.inRange(hsv, cul_inf, cul_sup)

    # Detectia obiectelor de culoare aflata in diapazon
    rezultat = cv.bitwise_and(img, img, mask=mask)

    cv.imshow("imagine", img)
    cv.imshow("Masca", mask)
    cv.imshow("Rezultat", rezultat)

    k = cv.waitKey(1) & 0xFF
    if k==27:
        break

cap.release() # se va folosi doar cand se va utiliza detectia obiectelor intr-un video
cv.destroyAllWindows()