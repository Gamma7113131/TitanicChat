function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    const chatBox = document.getElementById("chat-box");

    // Display user's message
    chatBox.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;

    // Send the user's input to the Flask backend
    fetch('/get', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `msg=${encodeURIComponent(userInput)}`,
    })
    .then(response => response.json())
    .then(data => {
        // Display bot's response
        chatBox.innerHTML += `<p><strong>TitanicBot:</strong> ${data.response}</p>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    });

    // Clear input field
    document.getElementById("user-input").value = '';
}
