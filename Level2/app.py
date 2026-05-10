from flask import Flask, jsonify, make_response, request
import jwt
import datetime

app = Flask(__name__)

WEAK_SECRET = "123456" 

@app.route('/')
def index():
    payload = {
        "role": "guest",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, WEAK_SECRET, algorithm="HS256")
    
    response = make_response(jsonify({
        "message": "Level 2: Weak Secret. You are currently a 'guest'.",
        "task": "Can you become 'admin' and access /admin_flag?",
        "hint": "The secret is weak. Brute-force is your friend."
    }))
    response.set_cookie("auth_token", token)
    return response

@app.route('/admin_flag')
def admin_flag():
    token = request.cookies.get('auth_token')
    if not token:
        return jsonify({"error": "No token provided"}), 401
    
    try:
        data = jwt.decode(token, WEAK_SECRET, algorithms=["HS256"])
        if data.get("role") == "admin":
            return jsonify({
                "flag": "flag{Weak_Secrets_Are_Easily_Cracked}",
                "congrats": "You cracked the secret and forged a token!"
            })
        else:
            return jsonify({"error": "Unauthorized. You are not admin!"}), 403
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid signature!"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)