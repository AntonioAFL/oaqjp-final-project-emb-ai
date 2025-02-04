from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index():
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_analyse():
    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyse)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion == None:
        return "Invalid text! Please try again!"

    output = f"For the fiven statment, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear},"
    output += f" 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."

    return output

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)