import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

cap = cv.VideoCapture("Trafic_rutier.mp4")

_, frame = cap.read()
x, y, w, h = 300, 200, 100, 50
fereastra_urmarire = x, y, w, h
# plt.imshow(frame)
# plt.show()

zona_interes = frame[y : y+h, x : x+w]
cv.imshow("Zona de interes", zona_interes)

zona_interes_hsv = cv.cvtColor(zona_interes, cv.COLOR_BGR2HSV)
masca = cv.inRange(zona_interes_hsv, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
zona_interes_hist = cv.calcHist([zona_interes_hsv], [0], masca, [180], [0, 180])
cv.normalize(zona_interes_hist, zona_interes_hist, 0, 255, cv.NORM_MINMAX)
criterii_term = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        zona_interes_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        destinatie = cv.calcBackProject([zona_interes_hsv], [0], zona_interes_hist, [0, 180], 1)
        ret, fereastra_urmarire = cv.CamShift(destinatie, fereastra_urmarire, criterii_term)
        puncte = cv.boxPoints(ret)
        puncte = np.int0(puncte)
        imagine = cv.polylines(frame, [puncte], True, (0, 255, 0), 2)

        cv.imshow("Trafic rutier", imagine)
        if cv.waitKey(20) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv.destroyAllWindows()