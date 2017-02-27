from flask import Flask, url_for
app = Flask(__name__)

@app.route('/wx')
def wx():
    return "hello is a test"

if __name__ == '__main__':
    app.run(debug=True)