import cv2
import numpy as np

class Preprocessing:
    def __init__(self) -> None:
        pass

    def doImageConversion(self, dict):
        dict = self.grayConversion(dict)

        dict = self.jpgConversion(dict)

        return dict


    def grayConversion(self, dict):
        image = dict['image']
        image = cv2.flip(image, 1)  # Mirror display
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        dict['image_gray'] = image
        image_proc = image[..., np.newaxis]        
        dict['image_proc'] = cv2.cvtColor(cv2.flip(image_proc, 1), cv2.COLOR_BGR2RGB)


    def jpgConversion(self, dict):
        return dict

