from GestureRecognition import MediapipeWrapper as mPipe
from GestureRecognition import HandGesture as hGesture
from GestureRecognition import PingerGesture as pGesture

class GestureRecogntion:

    def __init__(self) -> None:
        self.mPipe = mPipe.MediaPipeWrapper()
        self.hg = hGesture.HandGesture()
        self.pg = pGesture.PingerGesture()

    def doGestureRecogntion(self, dict):        

        # {'image':image, 'hands_info':results}
        dict = self.mPipe.searchHandPoint(dict)

        # {'image':image, 'hands_info':results, 'hand_sign_id':hand_sign_id}
        hgResult = self.hg.searchHandGesture(dict)

        # {'image':image, 'hands_info':results, 'hand_sign_id':hand_sign_id}
        pgResult = self.pg.serchPingerGesture(hgResult)

        return pgResult



        
