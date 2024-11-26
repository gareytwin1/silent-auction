const io = require("socket.io-client");

// Connect to the server
const socket = io("ws://127.0.0.1:5000");

socket.on("connect", () => {
    console.log("Connected to the server");

    // Emit a custom event with data
    socket.emit("custom_event", "Hello, this is a custom event from the client!");

    // Emit a broadcast event with data
    socket.emit("broadcast_event", "This message is broadcast to all clients.");
});

// Listen for server messages
socket.on("server_message", (data) => {
    console.log("Server message:", data.message);
});

// Listen for custom event response
socket.on("custom_event_response", (data) => {
    console.log("Custom event response:", data.message);
});

// Listen for broadcast response
socket.on("broadcast_response", (data) => {
    console.log("Broadcast response:", data.message);
});

// Handle disconnection
socket.on("disconnect", () => {
    console.log("Disconnected from the server");
});
