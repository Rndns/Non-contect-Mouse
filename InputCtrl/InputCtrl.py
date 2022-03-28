import cv2
import os

import util.plamode as pMode

# load, show, video

class InputCtrl:
    path_db = './video_db/test1.avi'
    path_img = './images/%s/frame%4d.jpg'
    dir = './images/%s'
    video = 'video'
    load = 'load'
    show = 'show'
    codec = 'DIVX'

    def __init__(self):
        pass

    # device(0) or db(name)
    def initialize(self, file = 0):
        if file == 0:
            self.capture = cv2.VideoCapture(0)
        else:
            self.fileName = file.split('/')[-1][:-4]
            self.count = 0
            os.makedirs(self.dir %(self.fileName), exist_ok=True)
            self.capture = cv2.VideoCapture(file)


    def finalize(self):
        self.capture.release()
        cv2.destroyAllWindows()


    def setPlaymode(self, play_mode=None):
        if play_mode == InputCtrl.video:
            self.play_mode = pMode.playmode.eVideo

        elif play_mode == InputCtrl.load:
            self.play_mode = pMode.playmode.eLoad

        elif play_mode == InputCtrl.show:
            self.play_mode = pMode.playmode.eShow

        else:
            assert 0


    def getPlaymode(self):
        return self.play_mode


    # play_mode(video, load, show)
    def doProcess(self):
        return self.capture.read()


    def keyProcess(self, key=-1, record=False, img=None):
        # Capture stop
        if key == 27: # ESC
            return False, record

        else:
            if self.play_mode == pMode.playmode.eVideo:
                record = self.makeDb(key, record=record, img=img)
            elif self.play_mode == pMode.playmode.eLoad:
                cv2.imwrite(InputCtrl.path_img %(self.fileName, self.count), img)
                self.count += 1
            return True, record


    def makeDb(self, key=-1, record=False, img=None):
        if (key == 114): # r
            self.video = cv2.VideoWriter(InputCtrl.path_db, cv2.VideoWriter_fourcc(*InputCtrl.codec), 30.0, (640, 480))
            record = True

        elif (key == 115) and record == True: # s
            self.video.release()
            return False

        if record == True:
            self.video.write(img)
            return True

        else:
            return False
