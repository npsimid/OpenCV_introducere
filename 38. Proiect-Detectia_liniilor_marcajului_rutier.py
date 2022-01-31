import cv2 as cv
import numpy as np

def regiune_interes(img, puncte):
    masca =np.zeros_like(img) # creaza o imagine neaagra de dimensiunea img
    potriv_color_masca = 255
    cv.fillPoly(masca, puncte, potriv_color_masca)
    img_mascata = cv.bitwise_and(img, masca)
    return img_mascata

def desenare_linii(img, linii):
    img = np.copy(img)
    img_alba = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)

    for linie in linii:
        for x1, y1, x2, y2, in linie:
            cv.line(img_alba, (x1, y1), (x2, y2), (0, 255, 0), 5)

    img = cv.addWeighted(img, 0.8, img_alba, 1, 0.0)
    return img

def procesare(img):
    inaltime = img.shape[0]
    latime = img.shape[1]

    puncte_regiune_interes = [(0, 0.92*inaltime),
                              (0.48*latime, 0.59*inaltime),
                              (latime, 0.92*inaltime)]

    alb_negru = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # tranformarea in alb-negru
    margini = cv.Canny(alb_negru, 50, 120) # detectarea marginilor
    img_taiata = regiune_interes(margini, np.array([puncte_regiune_interes], np.int32))

    linii = cv.HoughLinesP(img_taiata, 1, np.pi/180, 50, 100, 5) # determinarea coodonatelor a 2 puncte pentru fiecare linie

    img_linii = desenare_linii(img, linii)
    return img_linii

cap = cv.VideoCapture("sofare.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = procesare(frame)
        cv.imshow("imagine",frame)
        if cv.waitKey(10) & 0xFF== 27:
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
