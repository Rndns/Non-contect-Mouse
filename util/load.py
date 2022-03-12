import cv2

class Load:
    def __init__(self, name):
        self.name = name

    def movie(self):
        capture = cv2.VideoCapture(f'./video_db/{self.name}.avi')

        FPS = capture.get(cv2.CAP_PROP_FPS)
        delay = int(1000/FPS)

        while (capture.isOpened()):
            ret, frame = capture.read()

            # Image colorspace convert (Gray)
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

            # Image show
            cv2.imshow('to gray', gray)

            key = cv2.waitKey(delay)

            if key == 27:
                break  

        capture.release()
        cv2.destroyAllWindows()