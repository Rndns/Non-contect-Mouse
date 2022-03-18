import cv2

import util.plamode as pMode
import util.mediaPipe as mPipe

# load, show, video

class inputCtrl:
    path = './video_db/test0.avi'
    video = 'video'
    load = 'load'
    show = 'show'
    codec = 'DIVX'

    def __init__(self):
        self.mPipe = mPipe.MediaPipe()
    
    # device(0) or db(name)
    def initialize(self, file = 0):
        if file == 0:
            self.capture = cv2.VideoCapture(0)
        else:
            self.capture = cv2.VideoCapture(file)    


    def setPlaymode(self, play_mode=None):
        if play_mode == inputCtrl.video:
            self.play_mode = pMode.playmode.eVideo

        elif play_mode == inputCtrl.load:
            self.play_mode = pMode.playmode.eLoad

        elif play_mode == inputCtrl.show:
            self.play_mode = pMode.playmode.eShow

        else:
            assert 0


    def getPlaymode(self):
        return self.play_mode


    def finalize(self):
        self.capture.release()
        cv2.destroyAllWindows()

    # play_mode(video, load, show)
    def doProcess(self):
        # case 01
        # if self.play_mode == pMode.playmode.eVideo:
        #     return self.videoDb()

        # elif self.play_mode == pMode.playmode.eLoad or pMode.playmode.eShow:
        #     return self.showDb()

        # else:
        #     assert 0

        # case 02
        mDict = {0:self.videoDb(), 1:self.showDb(), 2:self.showDb}
        return mDict[self.play_mode.value]


    def videoDb(self):
        return self.capture.read()       

    # media pipe
    def showDb(self):
        ret, image = self.videoDb()
        return self.mPipe.handFrame(ret, image)

    # def videoWrite(self):
    #     return './video_db/test1.avi'


    def keyProcess(self, key=-1, record=False, img=None):
        # Capture stop
        if key == 27: # ESC
            return False, record

        else:
            if self.play_mode == pMode.playmode.eVideo:
                record = self.makeDb(key, record=record, img=img)
            return True, record


    def makeDb(self, key=-1, record=False, img=None):
        if (key == 114): # r
            self.video = cv2.VideoWriter(inputCtrl.path, cv2.VideoWriter_fourcc(*inputCtrl.codec), 30.0, (640, 480))
            record = True

        elif (key == 115) and record == True: # s
            self.video.release()
            return False

        if record == True:
            self.video.write(img)
            return True

        else:
            return False
