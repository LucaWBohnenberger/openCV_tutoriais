import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    imagem = np.zeros(frame.shape, np.uint8)
    small_frame = cv.resize(frame, (0,0), fx=0.5, fy=0.5)
    
    imagem[:height//2 , :width//2] = cv.rotate(small_frame, cv.ROTATE_180)
    imagem[height//2: , :width//2] = small_frame
    imagem[:height//2 , width//2:] = small_frame
    imagem[height//2: , width//2:] = cv.rotate(small_frame, cv.ROTATE_180)
    
    cv.imshow('frame', imagem)
    
    if cv.waitKey(1) == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()