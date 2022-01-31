import cv2 as cv

cascade_fete = cv.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")# definirea clasificatorului

cap = cv.VideoCapture("stiri.mp4")
while cap.isOpened():
    ret, img = cap.read()
    if ret:
        alb_negru = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        fete = cascade_fete.detectMultiScale(alb_negru, 1.1, 4)

        for x, y, w, h in fete:
            cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)

        cv.imshow("Rezultat", img)
        if cv.waitKey(1) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv.destroyAllWindows()