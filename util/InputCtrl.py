import cv2
import os

import util.plamode as pMode
import util.mediaPipe as mPipe

# load, show, video

class inputCtrl:
    path_db = './video_db/test1.avi'
    path_img = './images/%s/frame%4d.jpg'
    dir = './images/%s'
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
            self.fileName = file.split('/')[-1][:-4]
            self.count = 0
            os.makedirs(self.dir %(self.fileName), exist_ok=True)
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
        mDict = {0:self.videoDb(), 1:self.showDb(), 2:self.showDb()}
        return mDict[self.play_mode.value]


    def videoDb(self):
        return self.capture.read()       

    # media pipe
    def showDb(self):
        ret, image = self.videoDb()
        if not ret:
            return ret, image
        return self.mPipe.handFrame(ret, image)


    def keyProcess(self, key=-1, record=False, img=None):
        # Capture stop
        if key == 27: # ESC
            return False, record

        else:
            if self.play_mode == pMode.playmode.eVideo:
                record = self.makeDb(key, record=record, img=img)
            elif self.play_mode == pMode.playmode.eLoad:
                cv2.imwrite(inputCtrl.path_img %(self.fileName, self.count), img)
                self.count += 1
            return True, record


    def makeDb(self, key=-1, record=False, img=None):
        if (key == 114): # r
            self.video = cv2.VideoWriter(inputCtrl.path_db, cv2.VideoWriter_fourcc(*inputCtrl.codec), 30.0, (640, 480))
            record = True

        elif (key == 115) and record == True: # s
            self.video.release()
            return False

        if record == True:
            self.video.write(img)
            return True

        else:
            return False
