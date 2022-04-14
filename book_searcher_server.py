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

GRG = GR.GestureRecogntion(aws_enabler=True)

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

    if attr['MouseMode'] == 0:
        retData.hsign = gData.Data.HandSign.HandSign_open
        retData.fsign = gData.Data.FingerSign.FingerSign_stop
    elif attr['MouseMode'] == 1:
        retData.hsign = gData.Data.HandSign.HandSign_close
        retData.fsign = gData.Data.FingerSign.FingerSign_moving
    elif attr['MouseMode'] == 2:
        retData.hsign = gData.Data.HandSign.HandSign_oneFinger
        retData.fsign = gData.Data.FingerSign.FingerSign_moving
    elif attr['MouseMode'] == 3:
        retData.hsign = gData.Data.HandSign.HandSign_oneFinger
        retData.fsign = gData.Data.FingerSign.FingerSign_clockwise
    elif attr['MouseMode'] == 4:
        retData.hsign = gData.Data.HandSign.HandSign_oneFinger
        retData.fsign = gData.Data.FingerSign.FingerSign_counterClockwise 
    elif attr['MouseMode'] == 5:
        retData.hsign = gData.Data.HandSign.HandSign_oneFinger
        retData.fsign = gData.Data.FingerSign.FingerSign_moving

    for x, y in zip(attr['point_history'][-1][1], attr['point_history'][-1][2]):
        pointLoc = gData.Pointhistory()
        pointLoc.point.X_loc = x
        pointLoc.point.Y_loc = y
        retData.Point_History.append(pointLoc)

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