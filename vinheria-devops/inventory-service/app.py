from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/check', methods=['GET'])
def check_inventory():
    response = {
        "item_id": "Vinho-001",
        "available": True,
        "service": "InventoryService",
        "message": "Item is available."
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)