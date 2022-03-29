import cv2 as cv
import numpy as np
import csv
from util.CvFpsCalc import CvFpsCalc


class Visualize:
    def __init__(self) -> None:
        pass

    def showPoint(self, dict, draw):
        if not draw: 
            return dict['image']
        
        cvFpsCalc = CvFpsCalc(buffer_len=10)
        results = dict['handsInfo']

        if results.multi_hand_landmarks is None or results.multi_handedness is None:
            return dict['image']

        debug_image = dict['image']
        action = dict['MouseMode']

        use_brect = True  
        fps = cvFpsCalc.get()
        mode = 0
        number = -1

        with open('GestureRecognition/model/keypoint_classifier/keypoint_classifier_label.csv',
                encoding='utf-8-sig') as f:
            keypoint_classifier_labels = csv.reader(f)
            keypoint_classifier_labels = [row[0] for row in keypoint_classifier_labels]
        with open('GestureRecognition/model/point_history_classifier/point_history_classifier_label.csv',
                encoding='utf-8-sig') as f:
            point_history_classifier_labels = csv.reader(f)
            point_history_classifier_labels = [row[0] for row in point_history_classifier_labels]

        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            # Bounding box calculation
            brect = self.calc_bounding_rect(debug_image, hand_landmarks)

            # Drawing part
            debug_image = self.draw_bounding_rect(use_brect, debug_image, brect)
            debug_image = self.draw_info_text(
                debug_image,
                brect,
                handedness,
                keypoint_classifier_labels[dict['hand_sign_id']],
                point_history_classifier_labels[dict['finger_gesture_id']],
            )

        debug_image = self.draw_point_history(debug_image, dict['point_history'])
        debug_image = self.draw_info(debug_image, fps, mode, number, action)

        return debug_image


    def calc_bounding_rect(self, image, landmarks):
        image_width, image_height = image.shape[1], image.shape[0]

        landmark_array = np.empty((0, 2), int)

        for _, landmark in enumerate(landmarks.landmark):
            landmark_x = min(int(landmark.x * image_width), image_width - 1)
            landmark_y = min(int(landmark.y * image_height), image_height - 1)

            landmark_point = [np.array((landmark_x, landmark_y))]

            landmark_array = np.append(landmark_array, landmark_point, axis=0)

        x, y, w, h = cv.boundingRect(landmark_array)

        return [x, y, x + w, y + h]


    def draw_bounding_rect(self, use_brect, image, brect):
        if use_brect:
            # Outer rectangle
            cv.rectangle(image, (brect[0], brect[1]), (brect[2], brect[3]),
                        (0, 0, 0), 1)

        return image


    def draw_info_text(self, image, brect, handedness, hand_sign_text,
                    finger_gesture_text):
        cv.rectangle(image, (brect[0], brect[1]), (brect[2], brect[1] - 22),
                    (0, 0, 0), -1)

        info_text = handedness.classification[0].label[0:]
        if hand_sign_text != "":
            info_text = info_text + ':' + hand_sign_text
        cv.putText(image, info_text, (brect[0] + 5, brect[1] - 4),
                cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv.LINE_AA)

        if finger_gesture_text != "":
            cv.putText(image, "Finger Gesture:" + finger_gesture_text, (10, 60),
                    cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 4, cv.LINE_AA)
            cv.putText(image, "Finger Gesture:" + finger_gesture_text, (10, 60),
                    cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2,
                    cv.LINE_AA)

        return image


    def draw_point_history(self, image, point_history):
        for index, point in enumerate(point_history):
            if point[0] != 0 and point[1] != 0:
                cv.circle(image, (point[0], point[1]), 1 + int(index / 2),
                        (152, 251, 152), 2)

        return image


    def draw_info(self, image, fps, mode, number, action):
        cv.putText(image, "FPS:" + str(fps), (10, 30), cv.FONT_HERSHEY_SIMPLEX,
                1.0, (0, 0, 0), 4, cv.LINE_AA)
        cv.putText(image, "FPS:" + str(fps), (10, 30), cv.FONT_HERSHEY_SIMPLEX,
                1.0, (255, 255, 255), 2, cv.LINE_AA)
        
        cv.putText(image, "Action:" + action.name, (10, 430), cv.FONT_HERSHEY_SIMPLEX,
                1.0, (0, 0, 0), 4, cv.LINE_AA)
        cv.putText(image, "Action:" + action.name, (10, 430), cv.FONT_HERSHEY_SIMPLEX,
                1.0, (255, 255, 255), 2, cv.LINE_AA)
        

        mode_string = ['Logging Key Point', 'Logging Point History']
        if 1 <= mode <= 2:
            cv.putText(image, "MODE:" + mode_string[mode - 1], (10, 90),
                    cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1,
                    cv.LINE_AA)
            if 0 <= number <= 9:
                cv.putText(image, "NUM:" + str(number), (10, 110),
                        cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1,
                        cv.LINE_AA)
        return image


    def debugMode(self):
        pass

    def rockIcon(self):   
        pass

    def basicIcon(self):
        pass

    def circleIcon(self):
        pass

    def xIcon(self):
        pass