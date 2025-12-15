from flask import Flask, requests


app = Flask(__name__)

@app.route('/add')
def add():
    a = float(requests.get('a'))
    b = float(requests.get('a'))
    return a + b

if __name__ == "__main__":
    app.run()