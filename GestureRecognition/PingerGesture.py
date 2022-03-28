import copy
import itertools
from collections import deque
from collections import Counter

from GestureRecognition.model import PointHistoryClassifier


class PingerGesture:
    def __init__(self) -> None:
        pass

    # Main
    def serchPingerGesture(self, dict):

        point_history_classifier = PointHistoryClassifier()
        
        results = dict['handsInfo']
        debug_image = dict['image']
        point_history = dict['point_history']

        # Finger gesture history
        history_length = 16
        finger_gesture_history = deque(maxlen=history_length)

        if results.multi_hand_landmarks is not None:
            
            # normalized
            pre_processed_point_history_list = self.pre_process_point_history(debug_image, point_history)

            # Finger gesture classification
            finger_gesture_id = point_history_classifier(pre_processed_point_history_list)

            # Calculates the gesture IDs in the latest detection
            # finger_gesture_history.append(finger_gesture_id)

            # most_common_fg_id = Counter(
                # finger_gesture_history).most_common()
            
        else:
            finger_gesture_id = -1
        
        dict['finger_gesture_id'] = finger_gesture_id

        return dict


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
