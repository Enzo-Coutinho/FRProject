import serial

emotions = [0, 0, 0, 1, 0, 0, 0]

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.5)


def send():
    arduino.write(bytes(emotions))


def getter():
    return arduino.readline()

message = [6]
while True:
    send()
    print(str.replace((str)(getter()), r"\r\n", ""))
    arduino.flush()
