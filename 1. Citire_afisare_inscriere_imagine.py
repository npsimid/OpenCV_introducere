import cv2 as cv

#citirea imaginii
cale = "lena.jpg" #calea pina la imagine
flag= 1 # imagine in format BGR flag= 1, in format alb-negru flag=0, in format BGR+alpha(luminozitate) flag=-1
img =cv.imread(cale, flag)  # citirea imaginii ca np.array
print(img)

#afisarea imaginii
nume = "imagine" # denumirea ferestrei
cv.imshow(nume,img)  # afisarea imaginii
time = 0 # timpul de afisare a imagnii in ms, daca e 0 atunci e infinit
cv.waitKey(time) # fixare timp de afisare
cv.destroyAllWindows() #distrugera tuturor ferestrelor la finisarea timpului

#inscrierea unei imagini
cale_noua = "lena_copie.png" # fixarea cai si denumirii dorite a imaginii copiate
cv.imwrite(cale_noua, img) # salvarea imaginii copiate ca un fisier(se va iexecuta dupa inchiderea imaginii afisate)