import argparse
from statistics import mode
import cv2
import os

import util.InputCtrl as inpCtrl


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
    
    path = opt.db_path
    file_list = os.listdir(path)
    file_list_py = [path + '/' + file for file in file_list if file.endswith(".avi")]

    file_list_py = file_list_py if opt.play_mode == 'load' else [0]
    
    debug_mode = 0 if opt.debug_mode else 1

    inp = inpCtrl.intpuCtrl()

    for file in file_list_py:

        # class initialize
        inp.initialize(file)

        while True:
            # class process
            img = inp.doProcess(opt.play_mode)

            # debug_mode(Ture:0, False:1)
            key = cv2.waitKey(debug_mode)

            if not key:
                break

            cv2.imshow('hand', img)

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
                #cnt += 1
                #video.release()

            if record == True:
                video.write(frame)

        # class finalize
        inp.finalize()
