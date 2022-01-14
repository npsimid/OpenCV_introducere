import cv2 as cv

cap = cv.VideoCapture(0)

# citire dimensiuni
w = cap.get(cv.CAP_PROP_FRAME_WIDTH)  # citirea latimii imaginii
h = cap.get(cv.CAP_PROP_FRAME_HEIGHT)  # citirea inaltimii imaginii
print(w, h)

# setarea altor diemnsiuni
cap.set(3, 1208) # setarea altei latimi ( proprietatea CAP_PROP_FRAME_WIDTH poate fi substituita cu 3)
cap.set(4, 720) # setarea altei inaltimi ( proprietatea CAP_PROP_FRAME_HEIGHT poate fi substituita cu 4)

# citirea noilor dimensiuni
w = cap.get(cv.CAP_PROP_FRAME_WIDTH)  # citirea latimii imaginii
h = cap.get(cv.CAP_PROP_FRAME_HEIGHT)  # citirea inaltimii imaginii
print(w, h)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        # scrierea unui text cu dimensiunile video
        text = "Latimea: "+str(cap.get(3))+" Inaltimea: "+str(cap.get(4)) # precizarea textului
        frame = cv.putText(frame, text, (10,50), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2, cv.LINE_AA) # introducere text
        cv.imshow("frame", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
