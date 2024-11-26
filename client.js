const io = require("socket.io-client");

const socket = io("ws://127.0.0.1:5000");

socket.on("connect", () => {
    console.log("Connected to the server");
    // Emit a test message
    socket.emit("message", "Hello from the client");
});

socket.on("message", (data) => {
    console.log("Received message:", data.response || data);
});

socket.on("disconnect", () => {
    console.log("Disconnected from the server");
});
