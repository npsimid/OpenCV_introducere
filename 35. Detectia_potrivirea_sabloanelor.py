import cv2 as cv
import numpy as np

image=cv.imread("cats.jpg")
img = image.copy()
alb_negru = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
sablon = cv.imread("cat_sablon.jpg")
sablon_alb_negru = cv.cvtColor(sablon, cv.COLOR_BGR2GRAY)
w, h  = sablon_alb_negru.shape[::-1]  # determinara latimii mi inaltimii sablonului

metode = cv.TM_CCORR_NORMED # metoda de detectie si potrivire a sablonului

# determinarea tuturor punctelor ce ar putea fi punctul detectie a sablonului
rezultat =cv.matchTemplate(alb_negru, sablon_alb_negru, metode)
print(rezultat)
print(rezultat.max())

# selectarea unui singur punct (sau poate mai multe puncte) cu luminozitatea cea mai mare
loc = np.where(rezultat>=rezultat.max())
print(loc)

for punct in zip(*loc[::-1]): # se foloseste bucla pentru cazul in care sunt mai multe puncte ce pot contine potrivire
    cv.rectangle(img, punct, (punct[0]+w, punct[1]+h), (0,255,0), 3)

cv.imshow("Imagine", image)
cv.imshow("Sablon", sablon)
cv.imshow("Imagine cu sablon", img)
cv.waitKey(0)
cv.destroyAllWindows()