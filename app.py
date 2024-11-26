# app.py
import os
from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_socketio import SocketIO, emit # type: ignore
from flask_jwt_extended import JWTManager, create_access_token # type: ignore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auction.db'
app.config['SA_SECRET_KEY'] = 'dev' #'os.getenv('SA_SECRET_KEY')'

db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")
jwt = JWTManager(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    starting_bid = db.Column(db.Float, nullable=False)
    current_highest_bid = db.Column(db.Float, default=0)
    winner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    is_active = db.Column(db.Boolean, default=True)

class Bid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    bid_amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

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

# WebSocket
@app.route('/bids', methods=['POST'])
def place_bid():
    data = request.json
    user_id = data['user_id']
    item_id = data['item_id']
    bid_amount = data['bid_amount']
    # Validate bid and notify via WebSocket
    # Emit new bid to all clients
    socketio.emit('new_bid', {
        'item_id': user_id, 
        'current_highest_bid': bid_amount
    }, to='/')
    
    # Return a response
    return jsonify({'status': 'success', 'message': 'Bid placed successfully'}), 200

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
    socketio.emit("broadcast_response", {"message": data}, broadcast=True)

@socketio.on("message")
def handle_message(message):
    print("Received message:", message)
    socketio.send({"response": f"Server received: {message}"})

if __name__ == '__main__':
    socketio.run(app, debug=True)
