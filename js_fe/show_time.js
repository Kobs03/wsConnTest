window.addEventListener("DOMContentLoaded", () => {
    const messages = document.createElement("ul");
    document.body.appendChild(messages);

    const host = window.location.hostname; // Get the host IP dynamically
    const websocket = new WebSocket(`ws://${host}:5678/`);
    websocket.onmessage = ({ data }) => {
      const message = document.createElement("li");
      const content = document.createTextNode(data);
      message.appendChild(content);
      messages.appendChild(message);
    };
  });