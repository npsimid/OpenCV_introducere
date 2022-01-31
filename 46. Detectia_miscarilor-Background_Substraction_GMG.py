import cv2 as cv

cap = cv.VideoCapture("vtest.avi")
fgdg = cv.bgsegm.createBackgroundSubtractorGMG() # crearea unui obiect al background
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3)) # formarea unui nucleu pentru transformarea morfologica opening

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        masca_miscarilor = fgdg.apply(frame) # aplicarea obiectului background aupra imagiunii si formarea mastii miscarii
        masca_miscarilor=cv.morphologyEx(masca_miscarilor, cv.MORPH_OPEN, kernel) # realizarea opening=eroziunea apoi delatiunea

        cv.imshow("Original", frame)
        cv.imshow("Rezultat", masca_miscarilor)
        if cv.waitKey(30) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv.destroyAllWindows()