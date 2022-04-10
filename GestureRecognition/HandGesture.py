import copy
import itertools
import numpy as np

from collections import deque

from GestureRecognition.model import KeyPointClassifier
from util import MouseMode as mMode
from util import TritonClient as TC

class HandGesture:
    def __init__(self, aws_enabler) -> None:
        
        history_length = 16
        self.point_history = deque([[0,0]]*history_length, maxlen=history_length)

        self.aws_enabler = aws_enabler
        if aws_enabler:
            url = '172.17.0.3:8000'
            model_name = 'keypoint_onnx'
            self.tritonClient = TC.TritonClient(url, model_name)
        else:
            self.keypoint_classifier = KeyPointClassifier()

    def callKeypoint_onxx(self, input):
        # triton class
        input_np = np.array(input, dtype=np.float32).reshape(1,-1)
        output = np.array(self.tritonClient.callModel(input_np)['outputs'][0]['data'], dtype=np.float32)
        return np.argmax(np.squeeze(output))

    # Main
    def searchHandGesture(self, gesture):
        results = gesture['handsInfo']
        debug_image = gesture['image']
        gesture['hand_sign_id'] = 1


        if results.multi_hand_landmarks is None:
            self.point_history.append([0, 0])
            gesture['point_history'] = self.point_history
            gesture['MouseMode'] = mMode.MouseMode.eNothing
            return

        
        for hand_landmarks in results.multi_hand_landmarks:
            landmark_list = self.calc_landmark_list(debug_image, hand_landmarks)

            pre_processed_landmark_list = self.pre_process_landmark(
                landmark_list)

            # 0:open / 1:close / 2:finger
            if self.aws_enabler:
                hand_sign_id = self.callKeypoint_onxx(pre_processed_landmark_list)
            else:
                hand_sign_id = self.keypoint_classifier(pre_processed_landmark_list)
            # Point history
            if hand_sign_id == 1:  
                self.point_history.append(landmark_list[0])
                gesture['MouseMode'] = mMode.MouseMode.ePageScroll
            elif hand_sign_id == 2:
                self.point_history.append(landmark_list[8])
            else:
                self.point_history.append([0, 0])
                gesture['MouseMode'] = mMode.MouseMode.eNothing

    
        gesture['hand_sign_id'] = hand_sign_id
        gesture['point_history'] = self.point_history

        # return gesture


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



