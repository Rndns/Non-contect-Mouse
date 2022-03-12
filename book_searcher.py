import argparse
from statistics import mode
import util.video as video
import util.load as load
import util.show as show

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Book Searcher Mode')

    parser.add_argument('--play-mode',
                    required=False,
                    type=str,
                    default="record",
                    help='book searcher main mode')


    opt = parser.parse_args()

    #frame = movie, camera, 
    if opt.play_mode == "record":
        print("record mode")
        name = input('name:')
        video.Video(name).record()

    elif opt.play_mode == "camera":
        print("camera mode")
        show.Camera().cameraToGray()

    elif opt.play_mode == "movie":
        print('movie mode')
        name = input('name:')
        load.Load(name).movie()
        pass

    else:
        assert 0
