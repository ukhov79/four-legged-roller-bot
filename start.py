from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
    
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='192.168.1.38', threaded=True)
