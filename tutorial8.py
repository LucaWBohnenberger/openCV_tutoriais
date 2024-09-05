import numpy as np
import cv2 as cv

# Inicializa a captura de vídeo a partir da câmera (índice 0 para a câmera padrão)
cap = cv.VideoCapture(0)

# Carrega os classificadores em cascata pré-treinados para detecção de rostos e olhos
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')

while True:
    # Captura um frame do vídeo
    ret, frame = cap.read()
    
    # Converte o frame para escala de cinza para facilitar a detecção
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Detecta rostos no frame em escala de cinza
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Itera sobre cada rosto detectado
    for (x, y, w, h) in faces:
        # Desenha um retângulo ao redor do rosto detectado (cor azul, espessura 5)
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        
        # Define a região de interesse (ROI) para olhos dentro da região do rosto detectado
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        
        # Detecta olhos na região do rosto em escala de cinza
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        
        # Itera sobre cada olho detectado
        for (ex, ey, ew, eh) in eyes:
            # Desenha um retângulo ao redor do olho detectado (cor verde, espessura 5)
            cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)
    
    # Exibe o frame com rostos e olhos destacados
    cv.imshow('frame', frame)
    
    # Sai do loop se a tecla 'q' for pressionada
    if cv.waitKey(1) == ord('q'):
        break

# Libera a captura de vídeo e fecha todas as janelas abertas
cap.release()
cv.destroyAllWindows()
