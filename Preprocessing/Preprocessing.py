import cv2


class Preprocessing:
    def __init__(self) -> None:
        pass

    def doImageConversion(self, dict):
        dict = self.grayConversion(dict)

        dict = self.jpgConversion(dict)

        return dict


    def grayConversion(self, dict):
        dict['image'] = cv2.cvtColor(dict['image'], cv2.COLOR_RGB2GRAY)
        dict['image'] = cv2.cvtColor(dict['image'], cv2.COLOR_GRAY2RGB)
        return dict


    def jpgConversion(self, dict):
        return dict

