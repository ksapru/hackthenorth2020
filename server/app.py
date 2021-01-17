from flask import Flask
import time

import backend.api_calls as calls
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/output', methods=['GET'])
def getOutput():
    return {'output': 'the data'}
    
@app.route('/render')
def render_vid():
    video_path = "gs://prac_interview/testvideo.mp4"
    text = calls.get_video(video_path)
    sentiment = calls.text_sentiment(text)

    #returns percentage values
    percentages = calls.face_detect_video(gcs_uri=video_path)
    [smiling, looking_at_camera, eyes_visible] = percentages
    # TODO: figure out the best way to return all these variables
    print(f'text: {text}')
    print(f'sentiment: {sentiment}')
    print(f'smiling: {smiling}')
    print(f'looking at camera: {looking_at_camera}')
    print(f'eye visible {eyes_visible}')

    res = {
        "text": text,
        "sentiment": sentiment,
        "smiling": smiling,
        "looking_at_camera": looking_at_camera,
        "eyes_visible": eyes_visible
    }

    return res

if __name__ == '__main__':
    app.run()