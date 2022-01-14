import cv2 as cv
import numpy as np

# crearea unei imagini negre
latime = 512 #fixarea latimii imagini
inaltime = 512 # fixarea inaltimii imaginii
nr_canale=3 # fixarea numarului de canale
data_type= np.uint8 # ficarea tipului de date pentru fiecare pixel
img =np.zeros([latime, inaltime, nr_canale], data_type)

# Desenare linie
coord_incep = (0,0) # cordonatele punctului de inceput
coord_finis = (255,255) # cordonatele punctului de sfarsit
culoare = (255, 0, 0) # culoare in format albastru, verde, rosu
grosime = 2 # fixarea grosimii liniei
img =cv.line(img, coord_incep, coord_finis, culoare, grosime) # desenarea liniei

# Desenare linie cu sageata (la punctul de finis)
coord_incep2 = (430,250) # cordonatele punctului de inceput
coord_finis2 = (127,42) # cordonatele punctului de sfarsit
culoare2 = (0, 255, 0) # culoare in format albastru, verde, rosu
grosime2 = 5 # fixarea grosimii liniei
img =cv.arrowedLine(img, coord_incep2, coord_finis2, culoare2, grosime2) # desenarea liniei cu sageata

# Desenare dreptunghi
coord_incep3 = (234,167) # cordonatele punctului stanga sus
coord_finis3 = (256,432) # cordonatele punctului ddreapta jos
culoare3 = (0, 255, 255) # culoare in format albastru, verde, rosu
grosime3 = 3 # fixarea grosimii liniei, -1 va umple conturul
img = cv.rectangle(img, coord_incep3, coord_finis3, culoare3, grosime3) # desenarea dreptunghi

# Desenare cerc
coord_centru = (255,255) # cordonatele centrului
raza = 50 # raza cercului
culoare4 = (255, 0, 255) # culoare in format albastru, verde, rosu
grosime4 = -1 # fixarea grosimii liniei, -1 va umple conturul
img = cv.circle(img, coord_centru,raza, culoare4, grosime4) # desenare cerc

# introducere text
text= "OpenCV" # textul introdus
coord_inceput = (20,480) # coordonatele de inceput ale textului
font = cv.FONT_HERSHEY_SIMPLEX # selectarea fontului
dimens_font = 2 # dimensiunea fontului
culoare5 = (255, 255, 255) # culoare in format albastru, verde, rosu
grosime5 = 7 # fixarea grosimii liniei fontului
tipul_liniei = cv.LINE_AA # tipul liniei
img = cv.putText(img, text,coord_inceput, font, dimens_font, culoare5, grosime5, tipul_liniei) #introducere text

cv.imshow("imagine",img)

cv.waitKey(0)
cv.destroyAllWindows()
