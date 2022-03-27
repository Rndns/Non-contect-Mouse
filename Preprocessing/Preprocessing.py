class Preprocessing:
    def __init__(self) -> None:
        pass

    def doImageConversion(self, img):
        img_gray = self.grayConversion(img)

        img_jpg = self.jpgConversion(img_gray)

        return img_jpg

    def grayConversion(self, img):
        return img

    def jpgConversion(self, img):
        return img

