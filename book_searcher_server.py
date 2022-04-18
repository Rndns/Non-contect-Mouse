import typing
import uvicorn
from fastapi import FastAPI, Response, HTTPException, status, Header, Body, Depends
import GestureRecognition.GestureRecognition as GR
import ActionManager.ActionManager as Act

import cv2

import numpy as np

from proto_schema import imagePrep_pb2 as imgPrep
from proto_schema import gestureData_pb2 as gData

description = """
Encore python web server with Protobuf by ...
"""

app = FastAPI(
        title="book_sercher",
        description=description,
        version="0.0.2",
        contact={
        "e-mail" : "ddddddd@ggg.com"
    }
)

GRG = GR.GestureRecogntion(aws_enabler=True, url='172.17.0.2:8000')

def protoRead(serializedData) -> dict:
    return dict()


class ContentsTypeResponse(Response):
    media_type = 'application/encore'

def application_encore(content_type: str = Header(..., title="DDDDDD")):
    """Require request MIME-type to be application/encore"""

    #print(content_type)
    if content_type != ContentsTypeResponse.media_type:
        raise HTTPException(
            status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            f"Unsupported media type: {content_type}."
            " It must be application/encore",
        )

@app.post("/searching", dependencies=[Depends(application_encore)], \
                        response_class=ContentsTypeResponse )
async def gestureRecognation(pyload: bytes = Body(..., media_type = ContentsTypeResponse.media_type, \
                                            title="encore mentoring 2team",\
                                            description="dsklfjsldkfj", \
                                            example={"test":"ttt"},
                                        )):
    # proto read decode

    def protoRead(serializedData) -> dict:

        protoData = imgPrep.Image()
        protoData.ParseFromString(serializedData)
        
        def imgDecode(imgCompressed):
            encoded_img = np.fromstring(imgCompressed, dtype = np.uint8)
            return cv2.imdecode(encoded_img, cv2.IMREAD_UNCHANGED)

        attr = dict( {
            "image": imgDecode(protoData.gPicture)
        } )

        return attr

    attr = protoRead(pyload)

    # call GR
    GRG.doGestureRecognition(attr)
    # responce -proto
    retData = gData.Data()
    valMouseMode = attr['MouseMode'].value
    if valMouseMode == 0:
        retData.mouseMode = gData.Data.MouseMode.MouseMode_eNothing
        retData.hsign = gData.Data.HandSign.HandSign_open
        retData.fsign = gData.Data.FingerSign.FingerSign_stop
    elif valMouseMode == 1:
        retData.mouseMode = gData.Data.MouseMode.MouseMode_ePageScroll
        retData.hsign = gData.Data.HandSign.HandSign_close
        retData.fsign = gData.Data.FingerSign.FingerSign_moving
    elif valMouseMode == 2:
        retData.mouseMode = gData.Data.MouseMode.MouseMode_eClick
        retData.hsign = gData.Data.HandSign.HandSign_oneFinger
        retData.fsign = gData.Data.FingerSign.FingerSign_moving
    elif valMouseMode == 3:
        retData.mouseMode = gData.Data.MouseMode.MouseMode_eForwardPage
        retData.hsign = gData.Data.HandSign.HandSign_oneFinger
        retData.fsign = gData.Data.FingerSign.FingerSign_clockwise
    elif valMouseMode == 4:
        retData.mouseMode = gData.Data.MouseMode.MouseMode_eBackPage
        retData.hsign = gData.Data.HandSign.HandSign_oneFinger
        retData.fsign = gData.Data.FingerSign.FingerSign_counterClockwise 
    elif valMouseMode == 5:
        retData.mouseMode = gData.Data.MouseMode.MouseMode_eMouseControl
        retData.hsign = gData.Data.HandSign.HandSign_oneFinger
        retData.fsign = gData.Data.FingerSign.FingerSign_moving

    #for x, y in zip(attr['point_history'][-1][0], attr['point_history'][-1][1]):
    for point in attr['point_history']:
        retData.point.add(X_loc=point[0], Y_loc=point[1])
    
    if attr['handsInfo'].multi_hand_landmarks is None :
        retData.mark.add(x=0, y=0)
        return Response( retData.SerializeToString() )
    
    for landmark in attr['hand_landmarks']:
        retData.mark.add(x=landmark.x, y=landmark.y)

    return Response( retData.SerializeToString() )

if __name__ == "__main__":
    uvicorn.run(
        app='book_searcher_server:app',
        host="127.0.0.1",
        port=10011,
        workers=2,
        reload=True,
        debug=True
    )