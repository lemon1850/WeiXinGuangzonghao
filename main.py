from flask import Flask, url_for,request
import hashlib
import xml.etree.ElementTree as ET
import receive
app = Flask(__name__)
import reply
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

@app.route('/', methods=['POST'])
def wx2():
    xmlData = request.data;
    print(xmlData)
    recMsg = receive.parse_xml(xmlData);
    if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
        toUser = recMsg.FromUserName
        fromUser = recMsg.ToUserName
        content = "test"
        replyMsg = reply.TextMsg(toUser, fromUser, content)
        return replyMsg.send()
    return ""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=80)