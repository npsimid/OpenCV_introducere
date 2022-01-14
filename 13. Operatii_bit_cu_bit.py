import cv2 as cv
import numpy as np

# Crearea imaginii 1
img1=np.zeros((250,500,3), np.uint8) # imagine de culoarea neagra
img1 = cv.rectangle(img1, (200,0), (300,100), (255,255,255), -1) # desenarea unui dreptunghi alb

# Crearea imaginii 2
img2=np.zeros((250,500,3), np.uint8) # imagine de culoarea neagra
img2 = cv.rectangle(img2, (250,0), (500,500), (255,255,255), -1) # desenarea unui dreptunghi alb in a doua jumatate

# operatia SI bit cu bit
SI_bit = cv.bitwise_and(img1, img2)

# operatia SAU bit cu bit
SAU_bit = cv.bitwise_or(img1, img2)

# operatia SAU cu excludere bit cu bit
SAU_ex_bit = cv.bitwise_xor(img1, img2)

# operatia NU bit cu bit imagine 1
NU_bit1 = cv.bitwise_not(img1)

# operatia NU bit cu bit imagine 2
NU_bit2 = cv.bitwise_not(img2)

cv.imshow("image1", img1)
cv.imshow("image2", img2)
cv.imshow("SI_bit", SI_bit)
cv.imshow("SAU_bit", SAU_bit)
cv.imshow("SAU_ex_bit", SAU_ex_bit)
cv.imshow("NU_bit1", NU_bit1)
cv.imshow("NU_bit2", NU_bit2)
cv.waitKey(0)
cv.destroyAllWindows()