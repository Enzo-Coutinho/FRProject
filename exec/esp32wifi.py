from flask import Flask
import time

emotions = {}

esp32wifi = Flask(__name__)


def initserver():
   esp32wifi.run(host='0.0.0.0')  


def setemotions(emotes):
    global emotions
    emotions = emotes


@esp32wifi.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@esp32wifi.get("/emotions")
def getemote():
    return emotions

