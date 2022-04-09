from GestureRecognition import MediapipeWrapper as mPipe
from GestureRecognition import HandGesture as hGesture
from GestureRecognition import FingerGesture as fGesture

class GestureRecogntion:

    def __init__(self, aws_enabler) -> None:

        self.aws_enabler = aws_enabler

        self.mPipe = mPipe.MediaPipeWrapper()
        self.hg = hGesture.HandGesture(self.aws_enabler)
        self.pg = fGesture.FingerGesture(self.aws_enabler)

        

    def doGestureRecogntion(self, gesture):
        # {'image':image, 'hands_info':results}
        self.mPipe.searchHandPoint(gesture)

        # {'hand_sign_id':range(0,3)}
        self.hg.searchHandGesture(gesture)

        # {'finger_gesture_id':range(0,3)}
        self.pg.serchFingerGesture(gesture)

        
