
from flask import Flask
from flask.wrappers import Response
from flask.globals import request


import speech_recognition as sr

app = Flask(__name__)

recognizer = sr.Recognizer()


@app.route("/", methods=["GET"])
def index():
    return Response(
        {
            "response": "Make a post to `/recognize` with a attached wav audio, sampled at 16000hz with name audio"
        },
        content_type="application/json",
        status=200
    )


@app.route("/recognize", methods=["GET", "POST"])
def recognize():
    if request.method == "POST":
        if "audio" not in request.files:
            return Response(
                {"response": "You must specify an audio parameter with a wav file"},
                status=400
            )
        audio = sr.AudioData(request.files["audio"].read(), 16000, 1)

        hypothesis = recognizer.recognize_sphinx(
            audio,
            (
                'isolated_words_spa/words1.cd_semi_200',
                'isolated_words_spa/words1.lm.DMP',
                'isolated_words_spa/words1.dic'
            )
        )
        return Response(
            {
                "reponse": "Audio processed",
                "hypothesis": hypothesis
            }
        )
    else:
        return Response(
            {"response": "Please use the POST method and specify audio parameter with a wav file"},
            status=200
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000", debug=True)

