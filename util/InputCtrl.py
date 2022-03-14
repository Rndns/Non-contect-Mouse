import cv2
import os

# load, show, video

class intpuCtrl:
    def __init__(self) -> None:
        pass
    
    def initialize(self, file = None):
        if file == 0:
            self.capture = cv2.VideoCapture(0)
        else:
            self.capture = cv2.VideoCapture(file)    

    def finalize(self):
        self.capture.release()
        cv2.destroyAllWindows()

    def doProcess(self, play_mode="video"):
        if play_mode == "video":
            print("video mode")
            self.videoDb()

        elif play_mode == "load":
            print("load mode")            
            self.loadDb()

        elif play_mode == "show":
            print("show mode")
            return self.showDb()

        else:
            assert 0
        

    def videoDb(self):
        ret, frame = self.capture.read()

        if ret == False:
            return False

        return frame

    def loadDb(self):
        ret, frame = self.capture.read()

        if ret == False:
            return 

        # Image colorspace convert (Gray)
        # cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        return frame

    def showDb(self):
        ret, frame = self.capture.read()

        if ret == False:
            return 

        return False
