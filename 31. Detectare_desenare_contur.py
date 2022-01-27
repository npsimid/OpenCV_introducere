import cv2 as cv


img = cv.imread("OpenCV_Logo1.png")
img_alb_negru = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# limitarea la valoarea de prag pentru a detecta contururile

ret, prag = cv.threshold(img_alb_negru, 160, 255, 0)

# detectarea listei de contururi

modul = cv.RETR_TREE # modul conturului
metoda = cv.CHAIN_APPROX_NONE # metoda de aproximarea a contului
contururi,_ = cv.findContours(prag, modul, metoda)
print("Numarul contururilor: ", str(len(contururi)))
print(contururi[0])

# desenarea contururilor
n=-1 # numarul conturului desenat (-1  = toate contutururile)
culoare = (0, 255, 255)
grosime_linie = 3
cv.drawContours(img,contururi, n, culoare, grosime_linie)

cv.imshow("Imagine color", img)
cv.imshow("Imagine alb-negru", img_alb_negru)
cv.waitKey(0)
cv.destroyAllWindows()