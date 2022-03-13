import cv2

class Camera:
    def __init__(self) -> None:
        pass

    def cameraToGray(self):
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()

            if ret == False:
                break
            
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

            cv2.imshow('gray', gray)

            key = cv2.waitKey(1)

            if key == 27:
                break
        
        cap.release()
        cv2.destroyAllWindows()