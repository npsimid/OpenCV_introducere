import cv2 as cv
import numpy as np

def click_event(event, x, y, flags, param):
    if event==cv.EVENT_LBUTTONDOWN: # daca se apasa butonul stanga al mousului
        # se citeste valorilor pentru albastru, verde si rosu
        albastru = img[y, x, 0]
        verde = img[y, x, 1]
        rosu = img[y, x, 2]
        # se creaza un mic cerc in respectivul punct
        cv.circle(img, (x, y), 5, (255, 255, 0), 1)
        # Se creaza o imagine de culoare neagra
        img_culoare = np.zeros([512, 512, 3], np.uint8)
        # Se modifica culoarea neagra a imaginii in culoarea punctului selectat
        img_culoare[:]=[albastru, verde, rosu]
        cv.imshow("image_culoare", img_culoare)

# citirea unei imagini
img = cv.imread('lena.jpg')
cv.imshow("image", img)

# creara unei liste ce va contine punctele unde sa actionat clic
puncte = []

#Setarea eventului pentru mouse
cv.setMouseCallback("image", click_event)

cv.waitKey(0)
cv.destroyAllWindows()


