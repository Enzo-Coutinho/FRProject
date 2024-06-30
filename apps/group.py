import threading
import recognitioncv
import esp32serial

getExpressionThread = threading.Thread(target=recognitioncv.getRecog, daemon=True)
getExpressionThread.start()

MAX_PEOPLE = 1

while True:
    emotions = recognitioncv.getcount_emotions()
    emotions['r'] = (emotions['angry'] + emotions['sad']) * (255/MAX_PEOPLE)
    emotions['g'] = (emotions['neutral'] + emotions['happy']) * (255/MAX_PEOPLE)
    emotions['b'] = (emotions['tired']) * (255/MAX_PEOPLE)
    esp32serial.sendmessage(emotions)