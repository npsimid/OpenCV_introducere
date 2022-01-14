import cv2 as cv
import numpy as np

img =cv.imread("sudoku.png", 0)


# Threshold cu valorea de prag globala pentru toata imagine
_,pr1=cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# Threshold cu valorea de prag adaptiva pe portiuni de imagine
block_size=11 #dimensiunea blocului (conform teoriei)
constant = 2 # fixarea constantei (conform teoriei)

metoda1 = cv.ADAPTIVE_THRESH_MEAN_C # fixarea metodei de selectie a portiunilor pe imagine
pr2 = cv.adaptiveThreshold(img, 255, metoda1, cv.THRESH_BINARY, block_size,constant) # aplicarea metodei 1

metoda2 = cv.ADAPTIVE_THRESH_GAUSSIAN_C  # fixarea metodei de selectie a portiunilor pe imagine
pr3 = cv.adaptiveThreshold(img, 255, metoda2, cv.THRESH_BINARY, block_size,constant)  # aplicarea metodei 2

cv.imshow('imagine', img)
cv.imshow('Prag_1', pr1)
cv.imshow('Prag_2', pr2)
cv.imshow('Prag_3', pr3)

cv.waitKey(0)
cv.destroyAllWindows()