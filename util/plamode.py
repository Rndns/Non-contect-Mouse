from enum import Enum

class playmode(Enum):
    # video : local db 생성
    # show : capture from video -> mPipe -> imshow
    # load : load recored clip -> mPipe -> imshow

    eVideo = 0
    eShow = 1
    eLoad = 2