from asyncio import timeout

import serial
import json
import numpy as np
import cv2 as cv
from datetime import datetime

ser = serial.Serial('COM6', timeout=15)  # open serial port
while True:
    try:
        msg = ser.readline().decode(encoding="utf-8", errors="ignore")
        msg = msg.replace("'", '"')
        msg = '{"date":' + f'"{datetime.now()}"' + ', "plants":' + msg + '}'
        msg = json.loads(msg)
        print(msg)
        data = []
        with open('data_storage.json', 'a') as json_file:
            json.dump(msg, json_file,
                      indent=4,
                      separators=(',', ': '))

        count = 0
        cap = cv.VideoCapture(0)  # video capture source camera (Here webcam of laptop)
        ret, frame = cap.read()  # return a single frame in variable `frame`

            # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        date = datetime.now()
        date = f"{date}".replace('.','-').replace(' ','').replace(':','-')
        name = f"{date}.jpg"
        print(name)
        #cv.imwrite(name, frame)
        count += 1

        # When everything done, release the capture
        cap.release()

    except Exception as e:
        print(e)

ser.close()


