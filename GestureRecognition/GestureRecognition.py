import GestureRecognition.MediapipeWrapper as mPipe
import GestureRecognition.HandGesture as hGesture
import GestureRecognition.PingerGesture as pGesture


class GestureRecogntion:

    def __init__(self) -> None:
        self.mPipe = mPipe.MediaPipeWrapper()
        self.hg = hGesture.HandGesture()
        self.pg = pGesture.PingerGesture()

    def doGestureRecogntion(self, img):
        
        img, list = self.mPipe.searchHandPoint(img)

        int = self.hg.searchHandGesture(list)

        dict = self.pg.serchPingerGesture(int, list)

        return img, dict



        
