import cv2 as cv

def actiune(x):
    pass

img =cv.imread("gradient.png", 0) # doar in regim de alb-negru

cv.namedWindow("Reglare_prag")

# Bara de selectie a valorii de prag
cv.createTrackbar("Pragul","Reglare_prag", 0, 255, actiune)

# se creaza o bucla ce va permite reinoirea valorii de prag la modificarea valorii barei de selectie
while(1):
    val_prag = cv.getTrackbarPos("Pragul", "Reglare_prag") # valoarea de prag
    val_max = 255 # valoarea maxima

    # diferite tipuri de thresholding (prelucrarea in functie de valorea de prag)
    _,pr1=cv.threshold(img, val_prag, val_max, cv.THRESH_BINARY) # pina la prag - 0, dupa prag - 255
    _,pr2=cv.threshold(img, val_prag, val_max, cv.THRESH_BINARY_INV) # pina la prag - 255, dupa prag - 0
    _,pr3=cv.threshold(img, val_prag, val_max, cv.THRESH_TRUNC) # pina la prag - neschimbat, dupa prag - valoarea de prag
    _,pr4=cv.threshold(img, val_prag, val_max, cv.THRESH_TOZERO) # pina la prag - 0, dupa prag - neschimbat
    _,pr5=cv.threshold(img, val_prag, val_max, cv.THRESH_TOZERO_INV) # pina la prag - neschimbat, dupa prag - 0


    cv.imshow('imagine', img)
    cv.imshow('Prag_1', pr1)
    cv.imshow('Prag_2', pr2)
    cv.imshow('Prag_3', pr3)
    cv.imshow('Prag_4', pr4)
    cv.imshow('Prag_5', pr5)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()