import cv2
import mediapipe as mp


class MediaPipeWrapper:
    def __init__(self):
        pass

    def searchHandPoint(self, dict):
        mp_drawing = mp.solutions.drawing_utils
        mp_hands = mp.solutions.hands
        image = dict['image']
        
        with mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:

            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True   

        return {'image':image, 'handsInfo':results}

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
        return image, list