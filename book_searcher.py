import argparse
from statistics import mode
import util.video as video
import util.load as load
import util.show as show

import util.InputCtrl as inpCtrl

import cv2

import os

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Book Searcher Mode')

    parser.add_argument('--play-mode',
                    required=False,
                    type=str,
                    default="record",
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

    debug_mode = 1
    if opt.debug_mode == True:
        debug_mode = 0

    inp = inpCtrl.intpuCtrl()

    for file in file_list_py:
        # class initialize
        inp.initialize(file)

        while True:
            # class process
            img = inp.doProcess(opt.play_mode)

            # cv2.imshow('to gray', img)

            key = cv2.waitKey(1)

            # Capture stop
            if key == 27: # ESC
                break

            # Video recode start
            elif key == 114: # r
                record = True
                #video = cv2.VideoWriter(f'./video_db/{self.name}{cnt}.avi', fourcc, 30.0, (frame.shape[1], frame.shape[0]))
            
            # Video stop
            elif key == 115: # s
                record = False
                #cnt += 1
                #video.release()

        # class finalize
        inp.finalize()


    
    '''
    #frame = movie, camera, 
    if opt.play_mode == "record":
        print("record mode")
        #name = input('name:')        
        video.Video(opt.filename).record()

    elif opt.play_mode == "camera":
        print("camera mode")
        show.Camera().cameraToGray()

    elif opt.play_mode == "movie":
        print('movie mode')
        #name = input('name:')        
        for index, filename in enumerate(file_list_py):
            
            load.Load().movie(filename, debug_mode)
            print(f"{index} - {filename} proc done")
        pass

    else:
        assert 0
    '''
