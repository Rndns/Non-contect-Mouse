import mediapipe as mp
import cv2 as cv
import numpy as np

from util import TritonClient as TC


class MediaPipeWrapper:
    def __init__(self, aws_enabler, url):
        self.aws_enabler = aws_enabler

        if aws_enabler:
            url = url
            model_name = 'mediapipe_onnx'
            self.tritonClient = TC.TritonClient(url, model_name)

    def searchHandPoint(self, gesture):
        mp_hands = mp.solutions.hands
        debug_image = gesture['image']
        
        # if self.aws_enabler:
        #     self.callMeidapipe_onnx(gesture)

        with mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:

            debug_image.flags.writeable = False
            gesture['handsInfo'] = hands.process(debug_image)
            debug_image.flags.writeable = True
            
            if gesture['handsInfo'].multi_hand_landmarks is None :
                return
            
            gesture['hand_landmarks'] = gesture['handsInfo'].multi_hand_landmarks[0].landmark


    def callMeidapipe_onnx(self, gesture):
        resize_image = cv.resize(gesture['image'], dsize=[224, 224])
        input =  np.array(resize_image, dtype=np.float32).reshape((1,)+resize_image.shape)
        output = self.tritonClient.callModel(input)
        gesture['landmarks'] = np.array(output['outputs'][0]['data'])/224
        gesture['handFlag'] = output['outputs'][1]['data']
        gesture['handedness'] = output['outputs'][2]['data']
        



