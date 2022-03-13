import argparse
from statistics import mode
import util.video as video
import util.load as load
import util.show as show

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


# 폴더에 있는 파일을 전부 list 가져오기