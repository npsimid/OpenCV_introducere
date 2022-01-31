import cv2 as cv

cap = cv.VideoCapture("vtest.avi")
fgdg = cv.bgsegm.createBackgroundSubtractorMOG() # crearea unui obiect al background

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        masca_miscarilor = fgdg.apply(frame) # aplicarea obiectului background aupra imagiunii si formarea mastii miscarii

        cv.imshow("Original", frame)
        cv.imshow("Rezultat", masca_miscarilor)
        if cv.waitKey(20) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv.destroyAllWindows()