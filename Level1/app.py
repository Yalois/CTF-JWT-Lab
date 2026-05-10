from flask import Flask, jsonify, make_response
import jwt
import datetime

app = Flask(__name__)

SECRET_KEY = "level1-secret-key"

@app.route('/')
def index():
    payload = {
        "user": "guest",
        "role": "visitor",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        "flag": "flag{JWT_Data_Is_Visible_To_Everyone}",
        "hint": "JWT is just a base64 encoded JSON, it's not encrypted!"
    }

    # 生成 Token
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    # 构造响应
    response = make_response(jsonify({
        "status": "Welcome",
        "message": "Level 1: Information Disclosure. I've sent a gift to your cookies!",
        "task": "Decode the 'auth_token' cookie to find the flag."
    }))

    # 在进入 / 时自动设置 Cookie
    # httponly=False 是为了让新手也能通过 console (document.cookie) 查看到
    response.set_cookie("auth_token", token, httponly=False)

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
