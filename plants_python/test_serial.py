from asyncio import timeout

import serial
import json
import numpy as np
import cv2 as cv

ser = serial.Serial('COM6', timeout=15)  # open serial port
while True:
    try:
        msg = ser.readline().decode(encoding="utf-8", errors="ignore")
        msg = msg.replace("'", '"')
        json.loads(msg)
        print(msg)
        cap = cv.VideoCapture(0)
        if not cap.isOpened():
            print("Cannot open camera")
            exit()
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            # Our operations on the frame come here
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            color = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            # Display the resulting frame
            cv.imshow('frame', frame)
            if cv.waitKey(1) == ord('q'):
                break

        # When everything done, release the capture
        cap.release()
        cv.destroyAllWindows()
    except Exception as e:
        print(e)
ser.close()

