from GestureRecognition import MediapipeWrapper as mPipe
from GestureRecognition import HandGesture as hGesture
from GestureRecognition import FingerGesture as fGesture

class GestureRecogntion:

    def __init__(self, aws_enabler) -> None:
        self.mPipe = mPipe.MediaPipeWrapper()
        self.hg = hGesture.HandGesture()
        self.pg = fGesture.FingerGesture()

        self.aws_enabler = aws_enabler

    def doGestureRecogntion(self, gesture):        
        self.doGRAWS(gesture) if self.aws_enabler else self.doGRLocal(gesture)
        
    def doGRLocal(self, gesture):
        # {'image':image, 'hands_info':results}
        self.mPipe.searchHandPoint(gesture)

        # {'image':image, 'hands_info':results, 'hand_sign_id':hand_sign_id}
        self.hg.searchHandGesture(gesture)

        # {'image':image, 'hands_info':results, 'hand_sign_id':hand_sign_id}
        self.pg.serchFingerGesture(gesture)

    def doGRAWS(self, gesture):
        return NotImplemented





        
