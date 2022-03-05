import cv2

capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
record = False
name = 'test'

while True:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

    key = cv2.waitKey(1)
    
    # Capture stop
    if key == 27: # ESC
        break

    # Video recode start
    elif key == 114: # r
        record = True
        video = cv2.VideoWriter(f'./image_db/original/{name}.avi', fourcc, 30.0, (frame.shape[1], frame.shape[0]))
    
    # Video stop
    elif key == 115: # s
        record = False
        video.release()
    
    # Video save
    if record == True:
        video.write(frame)
        
capture.release()
cv2.destroyAllWindows()