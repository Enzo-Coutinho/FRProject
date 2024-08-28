from flask import Flask

emotions = {}

esp32wifi = Flask(__name__)


def setemotions(emotes):
    global emotions
    emotions = emotes


@esp32wifi.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@esp32wifi.get("/emotions")
def getemote():
    return emotions

def initserver():
   esp32wifi.run(host='0.0.0.0')  
