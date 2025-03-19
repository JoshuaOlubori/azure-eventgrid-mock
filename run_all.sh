#!/bin/bash

echo "==========================================="
echo "🛑 Killing existing services on ports 5000, 5001, and 5002..."
echo "==========================================="
lsof -ti :5000 -ti :5001 -ti :5002 | xargs kill -9 2>/dev/null || true
sleep 1

echo ""
echo "==========================================="
echo "🚀 Starting Event Broker on Port 5000..."
echo "==========================================="
python3 event_broker.py &  
sleep 2  

echo ""
echo "==========================================="
echo "🛒 Starting Order Processing Service on Port 5001..."
echo "==========================================="
python3 order_processor.py &  
sleep 2  

echo ""
echo "==========================================="
echo "📧 Starting Email Notification Service on Port 5002..."
echo "==========================================="
python3 email_service.py &  
sleep 2  

echo ""
echo "==========================================="
echo "🔗 Subscribing Services to Event Broker..."
echo "==========================================="
curl -X POST http://localhost:5000/subscribe -H "Content-Type: application/json" -d '{"eventType": "NewOrder", "endpoint": "http://localhost:5001/order-processor"}'
echo ""
curl -X POST http://localhost:5000/subscribe -H "Content-Type: application/json" -d '{"eventType": "NewOrder", "endpoint": "http://localhost:5002/email-service"}'
echo ""
sleep 2  

echo ""
echo "==========================================="
echo "📤 Publishing a Test Order Event..."
echo "==========================================="
python3 new_order_service.py  
sleep 2  

echo ""
echo "==========================================="
echo "✅ Setup Complete! Services Running..."
echo "==========================================="
