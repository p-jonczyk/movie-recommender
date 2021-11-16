"""With help of YT channal: DeepLearning_by_PhDScholar"""
import cv2 as cv
from deepface import DeepFace


def emotion_detector() -> str:
    """Detects emotion live via web camera with use of deepface 

    Returns: name of detected emotion """

    # use opencv file which is taken from github repository of opencv
    # haarcascade is face recognition algorithm
    face_cascade = cv.CascadeClassifier(
        cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cap = cv.VideoCapture(0)
    # if webcam opened correctly
    if not cap.isOpened():
        cap = cv.VideoCapture(1)
    if not cap.isOpened():
        raise IOError("Cannot find webcam")

    while(True):
        _, frame = cap.read()
        # obtain emotion from webcam
        result_dict = DeepFace.analyze(
            frame, actions=['emotion'], enforce_detection=False)

        # convert colors
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # draw rectangle around faces
        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 1)

        # set font
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(frame, result_dict['dominant_emotion'], (50, 60),
                   font, 2, (0, 255, 0), 2, cv.LINE_4)
        # right corner info
        cv.putText(frame, "Press 'space' to get current emotion...", (0, 320),
                   font, 1, (0, 0, 255), 2)

        cv.imshow('Emotion detector', frame)

        result = result_dict['dominant_emotion']

        if cv.waitKey(3) & 0xFF == ord(' '):
            break

    cap.release()
    cv.destroyAllWindows()
    return result


def main():
    result = emotion_detector()
    print(result)


if __name__ == '__main__':
    main()
