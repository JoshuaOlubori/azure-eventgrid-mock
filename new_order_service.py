import requests
import uuid
from datetime import datetime

EVENT_GRID_URL = "http://localhost:5000/publish"

def send_order_event():
    """Publish a New Order event to Event Grid."""
    event = {
        "id": str(uuid.uuid4()),
        "topic": "NewOrder",
        "eventType": "NewOrder.Created",
        "eventTime": datetime.utcnow().isoformat(),
        "data": {
            "orderId": "12345",
            "customerId": "67890",
            "orderValue": 150.00,
            "customerEmail": "customer@example.com"
        }
    }

    response = requests.post(EVENT_GRID_URL, json=event)
    print(f"Event published: {response.json()}")

# Send an event
send_order_event()
