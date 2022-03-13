import cv2
import os

# load, show, video

class intpuCtrl:
    def __init__(self) -> None:
        pass
    
    def initialize(self, filename = None):
        if filename is None:
            self.capture = cv2.VideoCapture(0)
        else:
            self.capture = cv2.VideoCapture(filename)
        

    def finalize(self):
        return NotImplemented

    def doProcess(self, play_mode="movie"):
        if play_mode == "record":
            print("record mode")
            #name = input('name:')        
            #video.Video(opt.filename).record()

            self.loadDb()

        elif play_mode == "camera":
            print("camera mode")            
            self.recordDb()

        elif play_mode == "movie":
            self.showDb()

        else:
            assert 0
        

    def recordDb(self):
        ret, frame = self.capture.read()

        if ret == False:
            return 

        return False

    def loadDb(self, dbPath):
        ret, frame = self.capture.read()

        if ret == False:
            return 

        # Image colorspace convert (Gray)
        self.gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        return False

    def showDb(self):
        ret, frame = self.capture.read()

        if ret == False:
            return 

        return False