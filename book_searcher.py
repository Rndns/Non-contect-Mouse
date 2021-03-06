import argparse
import cv2
import os

import InputCtrl.InputCtrl as inpCtrl
import util.plamode as pMode

import Preprocessing.Preprocessing as prepro
import GestureRecognition.GestureRecognition as gestureReco
import ActionManager.ActionManager as act
import Visualize.Visualize as visual


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected")




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Book Searcher Mode')

    parser.add_argument('--play-mode',
                    required=False,
                    type=str,
                    default="load",
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
                    type=str2bool,
                    default="False",
                    help='book searcher main mode')

    parser.add_argument('--debug-draw',
                    required=False,
                    type=str2bool,
                    default="False",
                    help='book searcher main mode')

    parser.add_argument('--aws-connect',
                    required=False,
                    type=str2bool,
                    default="False",
                    help='book searcher main mode')


    opt = parser.parse_args()
    
    path = opt.db_path
    file_list = os.listdir(path)
    file_list_py = [path + '/' + file for file in file_list if file.endswith(".avi")]

    file_list_py = file_list_py if opt.play_mode == 'load' else [0]
    
    debug_mode = 0 if opt.debug_mode else 30

    inp = inpCtrl.InputCtrl()
    inp.setPlaymode(opt.play_mode)

    prepro = prepro.Preprocessing()
    gestureReco = gestureReco.GestureRecogntion(opt.aws_connect)
    act = act.ActionManager()
    visual = visual.Visualize()

    for file in file_list_py:
        # class initialize
        inp.initialize(file)

        flag = True
        record = False
        gesture = {}

        while flag:
            # class process
            ret, img = inp.doProcess()

            if not ret:
                break

            # visual.setImage(img)
            gesture['image'] = img
            
            prepro.doImageConversion(gesture)
            
            gestureReco.doGestureRecognition(gesture)

            # gesture.drawResult(visual.getImage())
            act.doService(gesture)


            img = visual.showPoint(gesture, opt.debug_draw)

            # cv2.imshow('debuge', gesture['image_origin'])

            # debug_mode(Fraim: Ture(0) / False(1))
            key = cv2.waitKey(debug_mode)

            # ESC: close cap
            flag, record = inp.keyProcess(key, record, img)

        # class finalize
        inp.finalize()
