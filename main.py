from flask import Flask, url_for,request
import hashlib


app = Flask(__name__)

@app.route('/wx', methods=['POST'])
def wx():
    print(request.form.get("a"))
    print(request.form.get("a"))
    print(request.form.get("a"))
    print(request.data)
    print(request.args)
    print(request.base_url)
    print(request.cookies)

    return "hei"


if __name__ == '__main__':
    app.run(debug=True)