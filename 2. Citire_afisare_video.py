import cv2 as cv

input = 0  # sursa video poate fi:
           # 0 - prima camera,
           # 1 - a doua daca exista s.a.m.d
           # un string - cale catre un material video exemplu : input = "dog.mp4"
#input = "dog.mp4"

cap = cv.VideoCapture(input) # captarea secventelor video
file_exist = cap.isOpened()  # verificarea accesului la video
print(file_exist)

#citire dimensiuni
w = cap.get(cv.CAP_PROP_FRAME_WIDTH)  # citirea latimii imaginii
h = cap.get(cv.CAP_PROP_FRAME_HEIGHT)  # citirea inaltimii imaginii
print(w, h)


while (file_exist):
    ret, frame = cap.read() # citirea secventelor captate: frame - imaginea captata din video, ret = True daca imagnine exista
    if ret:
        cv.imshow("frame", frame) # afisarea imaginii frame in fereastra frame
        if cv.waitKey(1) & 0xFF == ord('q'): # inchidere fereastra cand se apasa tasta q
            break
    else:
        break
cap.release() # lansarea imaginilor captate
cv.destroyAllWindows() # distrugerea tuturor ferestrelor
