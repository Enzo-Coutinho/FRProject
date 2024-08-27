import serial
import json

class Esp32():
    
    def open(self):
        self.esp32 = serial.Serial(port='COM5', baudrate=115200, timeout=.5)
        self.message = None

    def getter(self):
        return self.esp32.readline()
    

    def sendmessage(self, message):
        self.esp32.write(bytes((json.dumps(message).encode())))
        self.esp32.flush()

    def close(self):
        self.esp32.flush()
        self.esp32.close()
