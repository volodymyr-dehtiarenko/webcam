import cv2


# Захват видео с вебкамеры и вывод
def video_webcam():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)                   # Номер камеры
    while True:
        cap.set(cv2.CAP_PROP_FPS, 35)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)  # Размер окна по ширине
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400) # Размер окна по высоте
        ret, img = cap.read()                   # Читаем с устройства кадр(картинку) , метод возвращает флаг ret (True , False) и img — саму картинку ( массив numpy).
        cv2.putText(img, "Recognize Face", (10, 40), cv2.FONT_ITALIC, 0.5, (255, 0, 0), 1)
        faces = face_cascade.detectMultiScale(img, minNeighbors=5, minSize=(10, 10))
        for (x, y, w, h) in faces:              # Квадрат вокруг лица
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
        cv2.imshow("camera", img)               # Функция imshow отображает изображение в указанном окне. Если окно не было создано, то создается новое. «camera» — имя окна , img — массив картинки.
        if cv2.waitKey(10) == 27:               # Клавиша Esc прерывает видео
            cap.release()
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    video_webcam()


