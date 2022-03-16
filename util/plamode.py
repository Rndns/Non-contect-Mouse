from enum import Enum

class playmode(Enum):
    # video : local db 생성
    # show : capture from video -> grat -> imshow
    # load : load recored clip -> gray -> imshow

    eVideo = 1
    eShow = 2
    eLoad = 3