import cv2 as cv
import numpy as np

events = [i for i in dir(cv) if "EVENT" in i] # formarea unei liste cu toate event-urile din cv2
print(events)

# creaarea unei functi ce va fi apelata cand se vor actiona butoanele mouse-ului
def click_event(event, x, y, flags, param): # functi primeste autoomat careva parametri; tipu event-ului, coorodnatele x,y, etc
    if event==cv.EVENT_LBUTTONDOWN: # daca se apasa butonul stanga al mousului
        # scrierea unui text cu coodonatele mouse-ului
        text = str(x) + " " + str(y)  # precizarea textului
        cv.putText(img, text, (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)  # introducere text
        cv.imshow("image", img)
    if event==cv.EVENT_RBUTTONDOWN: # daca se apasa butonul dreapta al mousului
        # citirea valorilor pentru albastru, verde si rosu
        albastru = img[y, x, 0] # citirea valorii culorii albastre a pixelului
        verde = img[y, x, 1] # citirea valorii culorii verzi a pixelului
        rosu = img[y, x, 2] # citirea valorii culorii rosii a pixelului
        text = str(albastru) + ", " + str(verde)+ ", " + str(rosu)  # precizarea textului
        cv.putText(img, text, (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 255), 2)  # introducere text
        cv.imshow("image", img)

# crearea unei imagini negre
img = np.zeros([512, 512, 3], np.uint8)
cv.imshow("image", img)

#Setarea eventului pentru mouse
cv.setMouseCallback("image", click_event)

cv.waitKey(0)
cv.destroyAllWindows()


