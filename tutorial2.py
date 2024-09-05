import cv2 as cv
import random

img = cv.imread('assets/map.jpg', -1)
img = cv.resize(img, (0,0), fx=3, fy=3)

#for i in range(100):
#   for j in range(img.shape[1]):
#        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

tag = img[300:450, 300:600]

img[0:150, 0:300] = tag
        
cv.imshow("Imagem", img)
cv.waitKey(0)
cv.destroyAllWindows
        
        
