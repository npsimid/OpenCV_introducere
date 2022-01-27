import cv2 as cv

cap = cv.VideoCapture("vtest.avi")

_, frame1 = cap.read()
_, frame2 = cap.read()

while cap.isOpened():
    diff = cv.absdiff(frame1, frame2) # detectia diferentei dintre primul si al doilea frame
    alb_negru = cv.cvtColor(diff, cv.COLOR_BGR2GRAY) # conversia in alb-negru
    blur = cv.GaussianBlur(alb_negru, (5,5), 0) #filtrea imagini alb-negru
    _, masca = cv.threshold(blur, 20, 255, cv.THRESH_BINARY) # craera masca prin filtrarea cu nivelul de prag
    delatiunea = cv.dilate(masca, None, iterations=3) # perfectionarea mastii
    contururi, _  = cv.findContours( delatiunea, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) # detectarea conturuilor
    #cv. drawContours(frame1, contururi, -1, (0,255,0), 2) # desenare contur pe frame 1

    for contur in contururi:
        x, y, w, h = cv. boundingRect(contur) # detrminare coordonate punct sus stanga, a latimi si a inaltimii contururilor
        aria_prag = 900 # fixarea ariei de prag cu care se va compara aria contururilor

        if cv.contourArea(contur) < aria_prag:
            continue # se sare peste contururile cu aria mai mica decat aria de prag
        cv.rectangle(frame1, (x,y), (x+w, y+h), (0, 255, 0), 2) # desenarea dreptunghiului in jurul contutului
        # cv.putText(frame1, "Miscare", (10, 20), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4) # plasare text in stanga sus a videoului

    cv.imshow("Cu contururi", frame1)
    frame1 = frame2 # trecerea la al doilea contur
    ret, frame2 = cap.read()
    if ret:
        if cv.waitKey(40) & 0xFF == 27:
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
