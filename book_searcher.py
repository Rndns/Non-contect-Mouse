import argparse
from statistics import mode
import cv2
import os

import util.InputCtrl as inpCtrl
import util.plamode as pMode


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Book Searcher Mode')

    parser.add_argument('--play-mode',
                    required=False,
                    type=str,
                    default="video",
                    help='book searcher main mode')
    
    parser.add_argument('--filename',
                    required=False,
                    type=str,
                    default="test0",
                    help='book searcher main mode')

    parser.add_argument('--db-path',
                    required=False,
                    type=str,
                    default="./video_db",
                    help='book searcher main mode')

    parser.add_argument('--debug-mode',
                    required=False,
                    type=bool,
                    default="False",
                    help='book searcher main mode')

    opt = parser.parse_args()

    print(pMode.playmode.eLoad)
    
    path = opt.db_path
    file_list = os.listdir(path)
    file_list_py = [path + '/' + file for file in file_list if file.endswith(".avi")]

    file_list_py = file_list_py if opt.play_mode == 'load' else [0]
    
    debug_mode = 0 if opt.debug_mode else 1

    inp = inpCtrl.intpuCtrl()
    inp.setPlaymode(opt.play_mode)

    for file in file_list_py:

        # class initialize
        inp.initialize(file)


        flag = True
        record = False

        while flag:
            # class process
            img, ret = inp.doProcess()
            if not ret:
                break

            cv2.imshow('hand', img)

            # debug_mode(Ture:0, False:1)
            key = cv2.waitKey(debug_mode)

            # ESC: close cap
            flag = inp.keyProcess(key)

            # video - r: start / s: stop
            #if opt.play_mode == 'video':
            #    record = inp.makeDb(key, record, img)

        # class finalize
        inp.finalize()
