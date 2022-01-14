import cv2 as cv

img =cv.imread("cats.jpg")
img2= cv.imread("opencv-logo.png")

# redimensionarea imaginilor (trebuie sa fie de aceleasi dimensiuni)
img = cv.resize(img, (512, 512))
img2 = cv.resize(img2, (512, 512))

# suprapunera imaginilor prin adunare
result= cv.add(img,img2)

# suprapunera imaginiilor prin fixarea ponderilor in rezultat
pondere_img1 = 0.9 # ponderea primei imagini
pondere_img2 = 0.1 # ponderea celei de a imagini
scalar = 0 # valoarea scalara care se va suma
result2 = cv.addWeighted(img, pondere_img1, img2, pondere_img2, scalar)

cv.imshow("image", result)
cv.imshow("image2", result2)
cv.waitKey(0)
cv.destroyAllWindows()