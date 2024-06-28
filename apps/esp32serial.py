import serial


esp32 = serial.Serial(port='COM5', baudrate=115200, timeout=.5)


def getter():
    return esp32.readline()


def sendmessage(x):
    esp32.write(bytes(x))
    print(str.replace((str)(getter()), r"\r\n", ""))
    esp32.flush()
