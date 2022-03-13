import cv2

class Load:
    def __init__(self, name = None):
        if name is not None:
            self.name = name


    def movie(self, name, debug_mode):
        capture = cv2.VideoCapture(name)

        # load class 카메라 정보에 의존성이 있나? -> No.
        FPS = 30 #capture.get(cv2.CAP_PROP_FPS)

        # divided by zero -> assert
        assert FPS != 0.0

        delay = int(1000/FPS)

        while (capture.isOpened()):
            ret, frame = capture.read()

            if ret == False:
                break 
            # Image colorspace convert (Gray)
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

            # Image show
            cv2.imshow('to gray', gray)

            key = cv2.waitKey(debug_mode)

            if key == 27:
                pass

        capture.release()
        cv2.destroyAllWindows()