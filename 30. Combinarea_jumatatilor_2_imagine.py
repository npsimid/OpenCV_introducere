import cv2 as cv
import numpy as np
apple = cv.imread("apple.jpg")
orange = cv.imread("orange.jpg")

print(apple.shape)
print(orange.shape)

# combinarea simpla prin taiere si alipire
apple_stanga_jum = apple[:, :256] # selectarea partii stangi a marului
orange_dreapta_jum = orange[:, 256:] # selectarea partii drepte a portocalei
apple_orange1 = np.hstack((apple_stanga_jum, orange_dreapta_jum)) # alipirea jumatatilor

# compinarea fina cu tehnicile piramidelor gauss si laplace

# generarea 6 imagini a marului cu rezolutii injumatatite (piramide gauss)
apple_copy = apple.copy()
gp_apple = [apple_copy] # crearea unei liste
for i in range(6):
    apple_copy = cv.pyrDown(apple_copy) #injumatatire rezolutie
    gp_apple.append(apple_copy) # adaugarea in lista

# generarea 6 imagini a portocalei cu rezolutii injumatatite (piramide gauss)
orange_copy = orange.copy()
gp_orange = [orange_copy] # crearea unei liste
for i in range(6):
    orange_copy = cv.pyrDown(orange_copy) #injumatatire rezolutie
    gp_orange.append(orange_copy) # adaugarea in lista

# generarea piramidelor Laplace pentru mar
apple_copy= gp_apple[5]
lp_apple = [apple_copy] # crearea unei liste
for i in range(5, 0, -1):
    gauss_restabilit = cv.pyrUp(gp_apple[i]) # restabilirea imaginii din rezolutia injumatatita
    laplace = cv.subtract(gp_apple[i-1], gauss_restabilit) # scaderea din original a imaginii restabilite
    lp_apple.append(laplace)


# generarea piramidelor Laplace pentru portocala
orange_copy= gp_orange[5]
lp_orange = [orange_copy] # crearea unei liste
for i in range(5, 0, -1):
    gauss_restabilit = cv.pyrUp(gp_orange[i]) # restabilirea imaginii din rezolutia injumatatita
    laplace = cv.subtract(gp_orange[i-1], gauss_restabilit) # scaderea din original a imaginii restabilite
    lp_orange.append(laplace)


# alipirea jumatatilor
apple_orange_piramid = []

for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    cols, row, ch = apple_lap.shape
    laplace = np. hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_piramid.append(laplace)
cv.imshow("combinarea inter", apple_orange_piramid[3])

# reconstructia
apple_orange_reconstruct = apple_orange_piramid[0]
for i in range(1,6):
    apple_orange_reconstruct = cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv. add(apple_orange_piramid[i],apple_orange_reconstruct)

cv.imshow("apple", apple)
cv.imshow("orange", orange)
cv.imshow("combinarea simpla", apple_orange1)

cv.imshow("combinarea fina", apple_orange_reconstruct)
cv.waitKey(0)
cv.destroyAllWindows()