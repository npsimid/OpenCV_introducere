import cv2 as cv

cap = cv.VideoCapture(0)
nume_file = "Inregistrare.mp4" # fixare numelui fisierului cu inregistrare
fourcc = cv.VideoWriter_fourcc(*'XVID') # tipul codecului pentru inregistrare
frame_per_sec = 20.0 # numarul de imagini pe secunda
formatul = (640, 480) # formatul continutului video
out = cv.VideoWriter(nume_file,fourcc, frame_per_sec, formatul) # initializarea obiectului cu inregistrarea

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        out.write(frame) # copierea fiecarei imagini
        cv.imshow("frame", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release() # lansarea imaginilor ccopiate
cv.destroyAllWindows()
