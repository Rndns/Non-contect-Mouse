import cv2
import numpy as np

class Preprocessing:
    def __init__(self) -> None:
        pass

    def doImageConversion(self, gesture):
        gesture = self.grayConversion(gesture)

        gesture = self.jpgConversion(gesture)

        return gesture


    def grayConversion(self, gesture):
        image = gesture['image']
        image_f = cv2.flip(image, 1)  # Mirror display
        gesture['image'] = image_f # Mirror display
        # image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        # gesture['image_gray'] = image
        # image_proc = image[..., np.newaxis]        
        gesture['image_proc'] = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)


    def jpgConversion(self, gesture):
        return gesture

