from flask import Flask
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/output', methods=['GET'])
def getOutput():
    return {'output': 'the data'}

if __name__ == '__main__':
    app.run()