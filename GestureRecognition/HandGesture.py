import copy
import itertools

from collections import deque

from GestureRecognition.model import KeyPointClassifier
from util import MouseMode as mMode

class HandGesture:
    def __init__(self) -> None:
        self.keypoint_classifier = KeyPointClassifier()

    # Main
    def searchHandGesture(self, dict):
        results = dict['handsInfo']
        debug_image = dict['image']
        dict['hand_sign_id'] = 1

        # Coordinate history 
        history_length = 16
        point_history = deque([[0,0]]*history_length, maxlen=history_length)

        if results.multi_hand_landmarks is None:
            point_history.append([0, 0])
            dict['point_history'] = point_history
            dict['MouseMode'] = mMode.MouseMode.eNothing
            return dict

        
        for hand_landmarks in results.multi_hand_landmarks:
            landmark_list = self.calc_landmark_list(debug_image, hand_landmarks)

            pre_processed_landmark_list = self.pre_process_landmark(
                landmark_list)

            # 0:rock / 1:open / 2:pinger
            hand_sign_id = self.keypoint_classifier(pre_processed_landmark_list)

            # Point history
            if hand_sign_id == 1:  
                point_history.append(landmark_list[0])
                dict['MouseMode'] = mMode.MouseMode.ePageScroll
            elif hand_sign_id == 2:
                point_history.append(landmark_list[8])
            else:
                point_history.append([0, 0])
                dict['MouseMode'] = mMode.MouseMode.eNothing

    
        dict['hand_sign_id'] = hand_sign_id
        dict['point_history'] = point_history

        return dict


    def calc_landmark_list(self, image, landmarks):
        image_width, image_height = image.shape[1], image.shape[0]

        landmark_point = []

        # Keypoint
        for _, landmark in enumerate(landmarks.landmark):
            landmark_x = min(int(landmark.x * image_width + 0.5), image_width - 1)
            landmark_y = min(int(landmark.y * image_height), image_height - 1)
            # landmark_z = landmark.z

            landmark_point.append([landmark_x, landmark_y])

        return landmark_point


    def pre_process_landmark(self, landmark_list):
        temp_landmark_list = copy.deepcopy(landmark_list)

        # Convert to relative coordinates
        
        base_x, base_y = 0, 0
        for index, landmark_point in enumerate(temp_landmark_list):
            if index == 0:
                base_x, base_y = landmark_point[0], landmark_point[1]

            temp_landmark_list[index][0] = temp_landmark_list[index][0] - base_x
            temp_landmark_list[index][1] = temp_landmark_list[index][1] - base_y
        
        '''
        base_x, base_y = landmark_point[0], landmark_point[1]
        index2 = 1
        for _, landmark_point in enumerate(temp_landmark_list[1:]):
            
            temp_landmark_list[index2][0] = temp_landmark_list[index2][0] - base_x
            temp_landmark_list[index2][1] = temp_landmark_list[index2][1] - base_y
            index2 += 1
        '''

        # Convert to a one-dimensional list
        temp_landmark_list = list(
            itertools.chain.from_iterable(temp_landmark_list))

        # Normalization
        max_value = max(list(map(abs, temp_landmark_list)))

        def normalize_(n):
            return n / max_value

        temp_landmark_list = list(map(normalize_, temp_landmark_list))

        return temp_landmark_list



