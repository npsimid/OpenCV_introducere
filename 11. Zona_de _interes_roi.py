import cv2 as cv

img =cv.imread("cats.jpg")


def click_event(event, x, y, flags, param):
    if event==cv.EVENT_LBUTTONDOWN:
        # daca se apasa butonul stanga al mousului se creaza un mic cerc in respectivul punct
        cv.circle(img, (x,y), 3, (0,255,0), -1)

        # adaugarea punctului in lista cu puncte
        puncte.append((x,y))

        #se verifica daca s-a dat click de 2 ori
        if len(puncte)==2:
            print(puncte)
            # se creaza un dreptunghi intre aceste 2 puncte
            cv.rectangle(img,puncte[-1], puncte[-2], (0,255,0), 2)

            # Crearea zonei de interes cuprinsa in dreptunghi
            zona_de_interes = img[puncte[0][1]:puncte[1][1], puncte[0][0]:puncte[1][0]]
            cv.imshow("zona", zona_de_interes)

            #inscrierea zonei de interes in coltul stanga de sus al imaginii
            img[0:abs(puncte[0][1]-puncte[1][1]), 0:abs(puncte[0][0]-puncte[1][0])]= zona_de_interes
            # print(zona_de_interes)

        # se curata lista daca se da click de mai mult de 2 ori
        if len(puncte)>=2:
            puncte.clear()

        cv.imshow("imagine", img)

cv.imshow('imagine', img)

# creara unei liste ce va contine punctele unde sa actionat clic
puncte = []

#Setarea eventului pentru mouse
cv.setMouseCallback("imagine", click_event)

cv.waitKey(0)
cv.destroyAllWindows()