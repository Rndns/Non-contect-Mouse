import cv2
import numpy as np
from proto_schema import gestureData_pb2 as gData, imagePrep_pb2 as imgPrep


class Preprocessing:
    def __init__(self) -> None:
        pass

    def doImageConversion(self, gesture):
        self.grayConversion(gesture)

        # protobuf
        return self.getSerializedData(gesture)
         


    def grayConversion(self, gesture):
        image = gesture['image']
        image_f = cv2.flip(image, 1)  # Mirror display
        gesture['image'] = image_f 
        # image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        # gesture['image_gray'] = image
        # image_proc = image[..., np.newaxis]        
        gesture['image_proc'] = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)


    def getSerializedData(self, gesture):
        protoData = imgPrep.Image()

        # imgData = cv2.imread(gesture['image']) # , cv2.IMREAD_GRAYSCALE)
        imgData = gesture['image']
        encode_param = [ int(cv2.IMWRITE_JPEG_QUALITY), 90 ]
        error, encimg = cv2.imencode('.jpg', imgData, encode_param)
        if error == False:
            assert 0

        protoData.gPicture = np.ndarray.tobytes( encimg )

        return protoData.SerializeToString()

