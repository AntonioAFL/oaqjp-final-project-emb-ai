"""
Emotion Detector Web Application.

This Flask application detects emotions from a given text input using 
the EmotionDetection module. It provides a web interface for users 
to analyze text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Instantiate the app
app = Flask(__name__)

@app.route("/")
def render_index():
    """Render the homepage.

    Returns:
        str: HTML content of the homepage.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def analyze_emotion():
    """Analyze emotions in the given text and return the result.

    Returns:
        str: A formatted emotional analysis or an error message.
    """
    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyse)

    anger = response.get("anger")
    disgust = response.get("disgust")
    fear = response.get("fear")
    joy = response.get("joy")
    sadness = response.get("sadness")
    dominant_emotion = response.get("dominant_emotion")

    if dominant_emotion is None:
        return "Invalid text! Please try again!", 400

    output = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return output


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
