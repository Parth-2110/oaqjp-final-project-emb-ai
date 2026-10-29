
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detector_route():
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "Please provide a statement to analyze!"

    response = emotion_detector(text_to_analyze)

    if isinstance(response, dict):
        result = response
    else:
        import json
        result = json.loads(response)

    if "dominant_emotion" in result:
        anger = result["anger"]
        disgust = result["disgust"]
        fear = result["fear"]
        joy = result["joy"]
        sadness = result["sadness"]
        dominant_emotion = result["dominant_emotion"]
    else:
        emotions = result["emotionPredictions"][0]["emotion"]
        anger = emotions["anger"]
        disgust = emotions["disgust"]
        fear = emotions["fear"]
        joy = emotions["joy"]
        sadness = emotions["sadness"]
        dominant_emotion = max(emotions, key=emotions.get)

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

