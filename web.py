import cv2
from reportlab.lib.colors import gray

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


    my_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors = 5,
        minSize = (10, 10)
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)


