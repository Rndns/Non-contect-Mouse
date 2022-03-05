import argparse
from statistics import mode

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Book Searcher Mode')

    parser.add_argument('--play-mode',
                    required=True,
                    type=str,
                    default="movie",
                    help='book searcher main mode')


    opt = parser.parse_args()

    #frame = movie, camera, 
    if opt.play_mode == "movie":
        print("recored mode")
        # movie load
        # inference test
    elif opt.play_mode == "camera":
        print("camera mode")
        # camera load
        # inferece test
    elif opt.play_mode == "record":
        # video.py
        # video class call
        pass
    else:
        assert 0


    while 1:
      
        # inference
        pass

        # if-else

    

        


    
