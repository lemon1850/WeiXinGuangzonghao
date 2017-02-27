from flask import Flask, url_for,request
import hashlib


app = Flask(__name__)

@app.route('/', methods=['GET'])
def wx():
    print(request.form.get("a"))
    print(request.form.get("a"))
    print(request.form.get("a"))
    print(request.data)
    print(request.args)
    print(request.base_url)
    print(request.cookies)
    text = request.args.get('echostr')

    return text


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=80)