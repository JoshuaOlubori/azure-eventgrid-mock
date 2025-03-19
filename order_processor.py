from flask import Flask, request

app = Flask(__name__)

@app.route('/order-processor', methods=['POST'])
def process_order():
    """Process the order event."""
    event = request.json
    print(f"📦 Processing Order: {event['data']}")
    return {"message": "Order processed"}, 200

if __name__ == '__main__':
    app.run(port=5001)
