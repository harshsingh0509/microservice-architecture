from flask import Flask, jsonify

app = Flask(__name__)

new_users = [
    {"user_id": 1, "name": "Alice", "role": "Admin"},
    {"user_id": 2, "name": "Bob", "role": "User"},
]

@app.route('/new-users', methods=['GET'])
def get_new_users():
    return jsonify(new_users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
