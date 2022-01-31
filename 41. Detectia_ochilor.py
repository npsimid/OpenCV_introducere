import cv2 as cv

cascade_fete = cv.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")# definirea clasificatorului fete
cascade_ochi = cv.CascadeClassifier("haarcascade/haarcascade_eye_tree_eyeglasses.xml")# definirea clasificatorului ochi

cap = cv.VideoCapture("Eu_inregistrare.mp4")
while cap.isOpened():
    ret, img = cap.read()
    if ret:
        alb_negru = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        fete = cascade_fete.detectMultiScale(alb_negru, 1.1, 4)

        for x, y, w, h in fete:
            cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)
            image_ochi = img[y:y + h, x:x + w]
            image_ochi_alb_negru = alb_negru[y:y+h, x:x+w]
            ochi = cascade_ochi.detectMultiScale(image_ochi_alb_negru)
            for xo, yo, wo, ho in ochi:
                cv.rectangle(image_ochi, (xo,yo), (xo+wo,yo+ho), (0, 255, 255), 3)

        cv.imshow("Rezultat", img)
        if cv.waitKey(1) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv.destroyAllWindows()