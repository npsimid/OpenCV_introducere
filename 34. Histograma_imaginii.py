import cv2 as cv
import matplotlib.pyplot as plt


img= cv.imread("lena.jpg")  # imaginea originala
alb_negru = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # imaginea alb-negru
albastru, verde, rosu = cv.split(img) # extragere canale albastru, verde, rosu

cv.imshow("Imaginea", img)
cv.imshow("Alb_negru", alb_negru)
cv.imshow("Canal albastru", albastru)
cv.imshow("Canal verde", verde)
cv.imshow("Canal rosu", rosu)

nr_max =256 # numarul mazim al valorilor pixelui
gama = [0, 256] # gama de valori

liniara_alb_negru = alb_negru.ravel() # aseaza toate liniile imaginii una dupa alta intr-o singura linie
liniara_albastru = albastru.ravel()
liniara_verde = verde.ravel()
liniara_rosu = rosu.ravel()

# construirea histogramei - adica a dependentei numarului de pixeli de valoarea lor
plt.hist(liniara_alb_negru, nr_max, gama)
plt.hist(liniara_albastru, nr_max, gama)
plt.hist(liniara_verde, nr_max, gama)
plt.hist(liniara_rosu, nr_max, gama)

# construirea graficului histogramei - doar a unei linii a nivelor valorilor poixelor
nr_canal = 0  # numarul canalui pentru care se construeste histograma (0 dac e alb negru si 0, 1, 2 daca e color)
masca = None # daca e alb negru nu trebuie masca

hist= cv.calcHist([alb_negru], [nr_canal], masca, [nr_max], gama)
plt.plot(hist)

plt.show()