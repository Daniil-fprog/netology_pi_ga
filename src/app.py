from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<a href="/add?a=1&b=2">add</a>'

@app.route('/add')
def add():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify(result=a + b), 200
    except ValueError:
        return jsonify(error="Invalid input"), 400


if __name__ == "__main__":
    app.run(debug=True)