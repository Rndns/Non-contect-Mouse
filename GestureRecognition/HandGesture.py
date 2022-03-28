import csv
import copy
import itertools

from GestureRecognition.model import KeyPointClassifier

class HandGesture:
    def __init__(self) -> None:
        pass

    # main
    def searchHandGesture(self, dict):
        keypoint_classifier = KeyPointClassifier()

        # with open('GestureRecognition/model/keypoint_classifier/keypoint_classifier_label.csv',
        #         encoding='utf-8-sig') as f:
        #     keypoint_classifier_labels = csv.reader(f)
        #     keypoint_classifier_labels = [
        #         row[0] for row in keypoint_classifier_labels
        #     ]

        results = dict['handsInfo']
        debug_image = dict['image']
        dict['hand_sign_id'] = 1

        # image = cv.flip(image, 1)  # Mirror display
        # debug_image = copy.deepcopy(image)

        if results.multi_hand_landmarks is not None:
            for hand_landmarks in results.multi_hand_landmarks:
                landmark_list = self.calc_landmark_list(debug_image, hand_landmarks)

                pre_processed_landmark_list = self.pre_process_landmark(
                    landmark_list)

                # hand_sign_id = keypoint_classifier(pre_processed_landmark_list)
                # 0:rock / 1:open / 2:pinger
                dict['hand_sign_id'] = keypoint_classifier(pre_processed_landmark_list)

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

        # Convert to a one-dimensional list
        temp_landmark_list = list(
            itertools.chain.from_iterable(temp_landmark_list))

        # Normalization
        max_value = max(list(map(abs, temp_landmark_list)))

        def normalize_(n):
            return n / max_value

        temp_landmark_list = list(map(normalize_, temp_landmark_list))

        return temp_landmark_list

    def test(self, img):
        a = img
        pass
