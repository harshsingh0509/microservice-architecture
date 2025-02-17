from flask import Flask, jsonify

app = Flask(__name__)

orders = [
    {"order_id": 1, "item": "Laptop", "quantity": 2},
    {"order_id": 2, "item": "Smartphone", "quantity": 1},
]

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
