import cv2
import os
import mediapipe as mp

#from util.video import Video
import util.plamode as pMode

# load, show, video

class intpuCtrl:
    def __init__(self) -> None:
        pass
    
    # device(0) or db(name)
    def initialize(self, file = 0):
        if file == 0:
            self.capture = cv2.VideoCapture(0)
        else:
            self.capture = cv2.VideoCapture(file)    

    def setPlaymode(self, play_mode="video"):
        if play_mode == "video":
            self.play_mode = pMode.playmode.eVideo

        elif play_mode == "load":
            self.play_mode = pMode.playmode.eLoad

        elif play_mode == "show":
            self.play_mode = pMode.playmode.eShow

        else :
            assert 0

    def getPlaymode(self):
        return self.play_mode


    def finalize(self):
        self.capture.release()
        cv2.destroyAllWindows()

    # play_mode(video, load, show)
    def doProcess(self):
        if self.play_mode == pMode.playmode.eVideo:
            return self.videoDb()

        elif self.play_mode == pMode.playmode.eLoad:
            return self.showDb()

        elif self.play_mode == pMode.playmode.eShow:
            return self.showDb()

        else:
            assert 0


    def videoDb(self):
        return self.capture.read()       

        #return ret, image

    # # load: load db
    # def loadDb(self):
    #     mp_drawing = mp.solutions.drawing_utils
    #     mp_hands = mp.solutions.hands
        
    #     with mp_hands.Hands(
    #         max_num_hands=1,
    #         min_detection_confidence=0.5,
    #         min_tracking_confidence=0.5) as hands:
        
    #         ret, image = self.capture.read()
    #         if not ret:
    #             return image, ret
    #         image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    
    #         results = hands.process(image)
    
    #         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    #         if results.multi_hand_landmarks:
    #             for hand_landmarks in results.multi_hand_landmarks:
    #                 finger1 = int(hand_landmarks.landmark[4].x * 100 )
    #                 finger2 = int(hand_landmarks.landmark[8].x * 100 )
    #                 dist = abs(finger1 - finger2)
    #                 cv2.putText(
    #                     image, text='f1=%d f2=%d dist=%d ' % (finger1,finger2,dist), org=(10, 30),
    #                     fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
    #                     color=255, thickness=3)
    
    #                 mp_drawing.draw_landmarks(
    #                     image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    #     # Image colorspace convert (Gray)
    #     return image, ret

    # media pipe
    def showDb(self):
        mp_drawing = mp.solutions.drawing_utils
        mp_hands = mp.solutions.hands
     
        
        with mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:
        
            ret, image = self.videoDb() #self.capture.read()
            if not ret:
                return image, ret
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    
            results = hands.process(image)
    
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                finger1 = int(hand_landmarks.landmark[4].x * 100 )
                finger2 = int(hand_landmarks.landmark[8].x * 100 )
                dist = abs(finger1 - finger2)
                cv2.putText(
                    image, text='f1=%d f2=%d dist=%d ' % (finger1,finger2,dist), org=(10, 30),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                    color=255, thickness=3)

                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        return image, ret


    def videoWrite(self):
        return


    def keyProcess(self, key=-1, record=False, img=None):
        # Capture stop
        if key == 27: # ESC
            return False

        else:
            if self.play_mode == pMode.playmode.eVideo:
                self.makeDb(key, record=record, img=img)
            return True 


    def makeDb(self, key=-1, record=False, img=None):
        if (key == 114): # r
            self.video = cv2.VideoWriter(f'./video_db/test3.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30.0, (640, 480))
            record = True

        elif (key == 115) and record == True: # s
            self.video.release()
            return False

        if record == True:
            self.video.write(img)
            return True

        else:
            return False
