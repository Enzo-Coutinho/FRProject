import serial
import json

esp32 = serial.Serial(port='COM5', baudrate=115200, timeout=.5)

jsEnc = json.JSONEncoder()

def getter():
    return esp32.readline()


def sendmessage(x):
    esp32.write(bytes((json.dumps(x).encode())))
    print(str.replace((str)(getter()), r"\r\n", ""))
    esp32.flush()
