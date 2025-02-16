from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users')
def get_users():
    users = [
        {"id": 1, "name": "Harsh"},
        {"id": 2, "name": "Saurav"}
    ]
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
