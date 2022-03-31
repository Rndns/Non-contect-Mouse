import copy
import itertools

from GestureRecognition.model import PointHistoryClassifier
from util import MouseMode as mMode


class FingerGesture:
    def __init__(self) -> None:
        self.point_history_classifier = PointHistoryClassifier()

    # Main
    def serchFingerGesture(self, gesture):
        
        results = gesture['handsInfo']
        debug_image = gesture['image']
        point_history = gesture['point_history']

        if results.multi_hand_landmarks is None:
            gesture['finger_gesture_id'] = -1
            self.seachMouseMode(gesture)
            # return gesture

        # normalized
        pre_processed_point_history_list = self.pre_process_point_history(debug_image, point_history)

        # Finger gesture classification
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
        
        if gesture['hand_sign_id'] != 2:
            return

        # if gesture['finger_gesture_id'] == 0:
        #     gesture['MouseMode'] = mMode.MouseMode.eClick
        # elif gesture['finger_gesture_id'] == 1:
        #     gesture['MouseMode'] = mMode.MouseMode.eForwardPage
        # elif gesture['finger_gesture_id'] == 2:
        #     gesture['MouseMode'] = mMode.MouseMode.eBackPage
        # elif gesture['finger_gesture_id'] == 3:
        #     gesture['MouseMode'] = mMode.MouseMode.eMouseControl
        # else:
        #     assert 0


        gestureValue = gesture['finger_gesture_id']

        assert( gestureValue < 4)

        gesture['MouseMode'] = mMode.MouseMode[gestureValue]
        

