from flask import Flask
import backend.api_calls as calls
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/render')
def render_vid():
    video_path = "gs://prac_interview/testvideo.mp4"
    text = calls.get_video(video_path)
    sentiment = calls.text_sentiment(text)
    print(sentiment)
    return text

if __name__ == '__main__':
    app.run()