import cv2
from time import sleep


def draw_label(img, text, pos, bg_color):
    font_face = cv2.FONT_HERSHEY_SIMPLEX
    scale = 0.6
    margin = 5
    text_size = cv2.getTextSize(text, font_face, scale, cv2.FILLED)
    end_x = pos[0] + text_size[0][0] + margin
    end_y = pos[1] - text_size[0][1] - margin
    cv2.rectangle(img, pos, (end_x, end_y), bg_color, cv2.FILLED)
    cv2.putText(img, text, pos, font_face, scale, (0, 0, 0), 1, cv2.LINE_AA)


casc_path = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(casc_path)

video_capture = cv2.VideoCapture(0)

while True:
    if not video_capture.isOpened():
        print('Unable to load camera')
        sleep(5)
        pass

    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=1,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        draw_label(frame, '<gender>', (x, y), (0, 255, 0))
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Turning off camera.")
        video_capture.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break


video_capture.release()
cv2.destroyAllWindows()