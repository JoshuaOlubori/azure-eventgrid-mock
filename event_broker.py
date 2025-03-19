from flask import Flask, request, jsonify
import threading
import requests

app = Flask(__name__)

# Store subscriptions (topic -> list of subscriber URLs)
subscriptions = {}

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Register a new subscriber to a topic."""
    data = request.json
    topic = data.get("topic")
    subscriber_url = data.get("subscriber_url")

    if topic not in subscriptions:
        subscriptions[topic] = []
    
    subscriptions[topic].append(subscriber_url)
    return jsonify({"message": f"Subscribed to {topic}"}), 200

@app.route('/publish', methods=['POST'])
def publish():
    """Publish an event to a topic."""
    event = request.json
    topic = event.get("topic")

    if topic in subscriptions:
        for subscriber_url in subscriptions[topic]:
            threading.Thread(target=send_event, args=(subscriber_url, event)).start()

    return jsonify({"message": "Event published"}), 200

def send_event(subscriber_url, event):
    """Send the event to a subscriber."""
    try:
        response = requests.post(subscriber_url, json=event)
        print(f"Sent event to {subscriber_url}: {response.status_code}")
    except Exception as e:
        print(f"Failed to send event: {e}")

if __name__ == '__main__':
    app.run(port=5000)
