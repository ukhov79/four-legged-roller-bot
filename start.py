from flask import Flask
import os
from sys import argv

# Получение ip адреса для запуска
script, ip = argv

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello!'
    
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host=ip, threaded=True, port=80)
