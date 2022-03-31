import mediapipe as mp


class MediaPipeWrapper:
    def __init__(self):
        pass

    def searchHandPoint(self, gesture):
        mp_hands = mp.solutions.hands
        debug_image = gesture['image_proc']
        
        with mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:

            #debug_image = cv2.cvtColor(cv2.flip(debug_image, 1), cv2.COLOR_BGR2RGB)

            debug_image.flags.writeable = False
            gesture['handsInfo'] = hands.process(debug_image)
            debug_image.flags.writeable = True 
