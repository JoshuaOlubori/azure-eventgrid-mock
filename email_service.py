from flask import Flask, request

app = Flask(__name__)

@app.route('/email-service', methods=['POST'])
def send_email():
    """Simulate sending an email notification."""
    event = request.json
    print(f"📧 Sending email to: {event['data']['customerEmail']}")
    return {"message": "Email sent"}, 200

if __name__ == '__main__':
    app.run(port=5002)
