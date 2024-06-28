from flask import Flask, render_template, Response, stream_with_context
import json
import time
from typing import Iterator
import apps.recognitioncv as recognitioncv 

app = Flask(__name__)




@app.route("/")
def hello_world():
    return render_template("webpageteamplate.html")



@app.route("/graph")
def graph():
    def returnJson() -> Iterator[str]:
        while True:
            recognitioncv.getRecog()
            json_data = json.dumps(recognitioncv.getcount_emotions())
            yield f"data:{json_data}\n\n"
            time.sleep(0.100)
    return Response(stream_with_context(returnJson()), mimetype="text/event-stream")


# recognitioncv.getRecog()

