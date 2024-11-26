# app.py
import os
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit # type: ignore
from flask_jwt_extended import JWTManager, create_access_token # type: ignore
from models import db, User, Item, Bid
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auction.db'
app.config['SA_SECRET_KEY'] = 'dev' #'os.getenv('SA_SECRET_KEY')'

db.init_app(app)
socketio = SocketIO(app, cors_allowed_origins="*")
jwt = JWTManager(app)

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    # Logic to register user (e.g., hashing password)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    # Logic to authenticate user and issue JWT

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.filter_by(is_active=True).all()
    return jsonify([item.to_dict() for item in items])

@app.route('/bids', methods=['POST'])
def place_bid():
    data = request.json
    user_id = data.get('user_id')
    item_id = data.get('item_id')
    bid_amount = data.get('bid_amount')

    # Validate the bid
    item = db.session.get(Item, item_id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    if bid_amount <= item.current_highest_bid:
        return jsonify({'error': 'Bid amount must be higher than the current bid'}), 400

    # Update the item's highest bid
    item.current_highest_bid = bid_amount
    item.winner_id = user_id
    db.session.commit()

    # Save the bid to the database
    new_bid = Bid(user_id=user_id, item_id=item_id, bid_amount=bid_amount)
    db.session.add(new_bid)
    db.session.commit()

    # Emit the new bid event
    socketio.emit('new_bid', {
        'item_id': item.id,
        'current_highest_bid': item.current_highest_bid,
        'winner_id': item.winner_id
    }, to=None)

    return jsonify({'message': 'Bid placed successfully!'})

# Handle connection
@socketio.on("connect")
def handle_connect():
    print("Client connected")
    emit("server_message", {"message": "Welcome to the server!"})

# Handle disconnection
@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected")

# Custom Event: Custom Message
@socketio.on("custom_event")
def handle_custom_event(data):
    print(f"Custom event received: {data}")
    emit("custom_event_response", {"message": f"Server received your custom event: {data}"})

# Custom Event: Broadcast to All Clients
@socketio.on("broadcast_event")
def handle_broadcast_event(data):
    print(f"Broadcasting: {data}")
    # Emit to all connected clients
    socketio.emit("broadcast_response", {"message": data}, to=None)


@socketio.on("message")
def handle_message(message):
    print("Received message:", message)
    socketio.send({"response": f"Server received: {message}"})

if __name__ == '__main__':
    socketio.run(app, debug=True)
