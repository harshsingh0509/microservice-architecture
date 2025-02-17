from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"user_id": 1, "name": "Harsh", "role": "Admin"},
    {"user_id": 2, "name": "Saurav", "role": "User"},
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
