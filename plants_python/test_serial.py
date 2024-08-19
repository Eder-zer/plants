import serial
import json

ser = serial.Serial('COM11')  # open serial port
while True:
    try:
        msg = ser.readline().decode(encoding="utf-8", errors="ignore")
        msg = msg.replace("'", '"')
        json.loads(msg)
        print(msg)
    except Exception as e:
        print(e)
ser.close()