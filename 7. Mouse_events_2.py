import cv2 as cv
import numpy as np


def click_event(event, x, y, flags, param):
    if event==cv.EVENT_LBUTTONDOWN: # daca se apasa butonul stanga al mousului
        # se creaza un mic cerc in respectivul punct
        cv.circle(img, (x,y), 5, (255,255,0), 1)
        puncte.append((x,y)) # adaugarea punctului in lista cu puncte
        #se verifica daca s-a dat click de mai multe ori
        if len(puncte)>=2:
            cv.line(img,puncte[-1], puncte[-2], (0,255,255), 2) # se creaza o lini intre ultime 2 puncte
        cv.imshow("image", img)

# crearea unei imagini negre
img = np.zeros([512, 512, 3], np.uint8)
cv.imshow("image", img)

# creara unei liste ce va contine punctele unde sa actionat clic
puncte = []

#Setarea eventului pentru mouse
cv.setMouseCallback("image", click_event)

cv.waitKey(0)
cv.destroyAllWindows()


