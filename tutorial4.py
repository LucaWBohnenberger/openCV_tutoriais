import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    #img = cv.line(frame, (0, 0), (width, height), (200, 100, 3), 10)
    img = cv.rectangle(frame, (30,20), (100, 80), (0, 100, 250), -1)  
    img = cv.circle(frame, (400, 80), 80, -1)
    font = cv.FONT_HERSHEY_DUPLEX
    img = cv.putText(frame, "Hello World", (100, 300), font, 2, (10, 50, 240), 2, cv.LINE_AA)
    
    
    cv.imshow('frame', img)
    
    if cv.waitKey(1) == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()