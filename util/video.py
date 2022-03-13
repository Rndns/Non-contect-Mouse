import cv2
import os


class Video:
    def __init__(self, name) -> None:
        self.name = name

    def record(self):

        os. makedirs('video_db', exist_ok=True)

        capture = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        record = False

        cnt = 0

        while True:
            ret, frame = capture.read()
            cv2.imshow("VideoFrame", frame)

            if ret == False:
                break

            key = cv2.waitKey(1)
            
            # Capture stop
            if key == 27: # ESC
                break

            # Video recode start
            elif key == 114: # r
                record = True
                video = cv2.VideoWriter(f'./video_db/{self.name}{cnt}.avi', fourcc, 30.0, (frame.shape[1], frame.shape[0]))
            
            # Video stop
            elif key == 115: # s
                record = False
                cnt += 1
                video.release()
            
            # Video save
            if record == True:
                video.write(frame)
                
        capture.release()
        cv2.destroyAllWindows()
