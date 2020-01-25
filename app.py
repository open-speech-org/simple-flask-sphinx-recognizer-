from flask import Flask
from flask.globals import request


import speech_recognition as sr

app = Flask(__name__)

recognizer = sr.Recognizer()


@app.route("/", methods=["GET"])
def index():
    return {
        "response": "Make a post to `/recognize` with a attached wav audio, sampled at 16000hz with name audio"
    }


@app.route("/recognize", methods=["GET", "POST"])
def recognize():
    if request.method == "POST":
        if "audio" not in request.files:
            return (
                {
                    "response": "You must specify an audio parameter with a wav file"
                },
                400
            )
        audio_file = sr.AudioFile(request.files["audio"])
        with audio_file as source:
            audio = recognizer.record(source)
            hypothesis = recognizer.recognize_sphinx(
                audio,
                (
                    'isolated_words_spa/words1.cd_semi_200',
                    'isolated_words_spa/words1.lm.DMP',
                    'isolated_words_spa/words1.dic'
                )
            )
            print(hypothesis)
        return {
            "reponse": "Audio processed",
            "hypothesis": hypothesis
        }

    else:
        return {
            "response": "Please use the POST method and specify audio parameter with a wav file"
        }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000", debug=True)

