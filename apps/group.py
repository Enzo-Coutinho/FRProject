import threading
import recognitioncv
import esp32serial

getExpressionThread = threading.Thread(target=recognitioncv.getRecog, daemon=True)
getExpressionThread.start()

while True:
    esp32serial.sendmessage(recognitioncv.getcount_emotionsarray())