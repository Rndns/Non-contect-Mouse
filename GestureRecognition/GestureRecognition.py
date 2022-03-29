from GestureRecognition import MediapipeWrapper as mPipe
from GestureRecognition import HandGesture as hGesture
from GestureRecognition import PingerGesture as pGesture

class GestureRecogntion:

    def __init__(self) -> None:
        self.mPipe = mPipe.MediaPipeWrapper()
        self.hg = hGesture.HandGesture()
        self.pg = pGesture.PingerGesture()

        self.aws_enabler = False

    def doGestureRecogntion(self, dict):        
        self.doGRAWS(dict) if self.aws_enabler else self.doGRLocal(dict)
        
    def doGRLocal(self, dict):
        # {'image':image, 'hands_info':results}
        self.mPipe.searchHandPoint(dict)

        # {'image':image, 'hands_info':results, 'hand_sign_id':hand_sign_id}
        self.hg.searchHandGesture(dict)

        # {'image':image, 'hands_info':results, 'hand_sign_id':hand_sign_id}
        self.pg.serchFingerGesture(dict)

    def doGRAWS(self, dict):
        return NotImplemented





        
