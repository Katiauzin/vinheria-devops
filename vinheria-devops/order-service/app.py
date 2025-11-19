from flask import Flask, jsonify, make_response
import requests

app = Flask(__name__)

INVENTORY_SERVICE_URL = 'http://inventory_service:5001/inventory/check'

@app.route('/create', methods=['POST'])
def create_order():
    try:
        inventory_response = requests.get(INVENTORY_SERVICE_URL)
        
        if inventory_response.status_code == 200 and inventory_response.json().get('available'):
            return make_response(jsonify({
                "status": "Order Created",
                "inventory_check": inventory_response.json(),
                "message": "Order processed and inventory confirmed."
            }), 201)
        else:
            return make_response(jsonify({"status": "Failed", "message": "Inventory check failed or item unavailable."}), 400)

    except requests.exceptions.ConnectionError:
        return make_response(jsonify({"status": "Error", "message": "Cannot connect to Inventory Service. Service Discovery failed or service is down."}), 503)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)