import copy
import itertools
import numpy as np

from GestureRecognition.model import PointHistoryClassifier
from util import MouseMode as mMode
from util import TritonClient as TC


class FingerGesture:
    def __init__(self, aws_enabler) -> None:
        
        self.aws_enabler = aws_enabler
        
        if aws_enabler:
            url = '172.17.0.3:8000'
            model_name = 'pointHistory_onnx'
            self.tritonClient = TC.TritonClient(url, model_name)
        else:
            self.point_history_classifier = PointHistoryClassifier()


    def callPointHistory_onnx(self, input):
        input_np = np.array(input, dtype=np.float32).reshape(1,-1)
        output = self.tritonClient.callModel(input_np)
        return np.argmax(np.squeeze(output))

    # Main
    def serchFingerGesture(self, gesture):
        
        results = gesture['handsInfo']
        debug_image = gesture['image']
        point_history = gesture['point_history']

        if results.multi_hand_landmarks is None:
            gesture['finger_gesture_id'] = -1
            self.seachMouseMode(gesture)
            return

        # normalized
        pre_processed_point_history_list = self.pre_process_point_history(debug_image, point_history)

        # Finger gesture classification
        if self.aws_enabler:
            gesture['finger_gesture_id'] = self.callPointHistory_onnx(pre_processed_point_history_list)
        else:
            gesture['finger_gesture_id'] = self.point_history_classifier(pre_processed_point_history_list)
        
        self.seachMouseMode(gesture)

        # return gesture


    def pre_process_point_history(self, image, point_history):
        image_width, image_height = image.shape[1], image.shape[0]

        temp_point_history = copy.deepcopy(point_history)

        # Convert to relative coordinates
        base_x, base_y = 0, 0
        for index, point in enumerate(temp_point_history):
            if index == 0:
                base_x, base_y = point[0], point[1]

            temp_point_history[index][0] = (temp_point_history[index][0] -
                                            base_x) / image_width
            temp_point_history[index][1] = (temp_point_history[index][1] -
                                            base_y) / image_height

        # Convert to a one-dimensional list
        temp_point_history = list(
            itertools.chain.from_iterable(temp_point_history))

        return temp_point_history

    
    def seachMouseMode(self, gesture):
        # assert(gesture['finger_gesture_id']!=0)
        # print(gesture['finger_gesture_id'])
        # print(gesture['hand_sign_id'])

        if( gesture['finger_gesture_id'] == 2) :
            a = 12

        if gesture['hand_sign_id'] != 2:
            return

        # gestureValue = gesture['finger_gesture_id']

        # assert( gestureValue < 4)

        # gesture['MouseMode'] = mMode.MouseMode[gestureValue]
        
        if gesture['finger_gesture_id'] == 0:
            gesture['MouseMode'] = mMode.MouseMode.eClick
        elif gesture['finger_gesture_id'] == 1:
            gesture['MouseMode'] = mMode.MouseMode.eForwardPage
        elif gesture['finger_gesture_id'] == 2:
            gesture['MouseMode'] = mMode.MouseMode.eBackPage
        elif gesture['finger_gesture_id'] == 3:
            gesture['MouseMode'] = mMode.MouseMode.eMouseControl
        else:
            assert 0


        

