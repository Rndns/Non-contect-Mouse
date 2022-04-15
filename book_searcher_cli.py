import argparse
import cv2
import os
import requests


from proto_schema import gestureData_pb2 as gData, imagePrep_pb2 as imgPrep
import InputCtrl.InputCtrl as inpCtrl
import util.plamode as pMode
import Preprocessing.Preprocessing as prepro
import GestureRecognition.GestureRecognition as gestureReco
import ActionManager.ActionManager as act
import Visualize.Visualize as visual
import util.MouseMode as mMode


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

    print(pMode.playmode.eLoad, opt.play_mode)
    
    path = opt.db_path
    file_list = os.listdir(path)
    file_list_py = [path + '/' + file for file in file_list if file.endswith(".avi")]

    file_list_py = file_list_py if opt.play_mode == 'load' else [0]
    
    debug_mode = 0 if opt.debug_mode else 30

    inp = inpCtrl.InputCtrl()
    inp.setPlaymode(opt.play_mode)

    oPrepro = prepro.Preprocessing()
    oGestureReco = gestureReco.GestureRecogntion(opt.aws_connect)
    oAct = act.ActionManager()
    oVisual = visual.Visualize()


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
            
            # Image preprocess
            protoData = oPrepro.doImageConversion(gesture)

            headers = {'Content-Type': 'application/encore'}
            response = requests.post( \
                url="http://127.0.0.1:10011/searching", \
                headers=headers, \
                data=protoData  \
                )

            if response.status_code == 200 :
                response.raise_for_status()
                retData = gData.Data()
                retData.ParseFromString( response.content )
                print(retData)
            else:
                print(f"Error : {response.status_code}")

            # gesture.drawResult(visual.getImage())
            gesture['MouseMode'] = mMode.MouseMode(retData.mouseMode)
            gesture['hand_sign_id'] = retData.hsign
            gesture['finger_sign_id'] = retData.fsign
            gesture['point_history'] = [ [data.X_loc, data.Y_loc] for data in retData.point ]

            oAct.doService(gesture)


            img = oVisual.showPoint(gesture, opt.debug_draw)

            # cv2.imshow('debuge', gesture['image'])

            # debug_mode(Fraim: Ture(0) / False(1))
            key = cv2.waitKey(debug_mode)

            # ESC: close cap
            flag, record = inp.keyProcess(key, record, img)

        # class finalize
        inp.finalize()
                    



