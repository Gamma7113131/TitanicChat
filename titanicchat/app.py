import os
import subprocess
import sys
import webbrowser
from flask import Flask, render_template, request, jsonify
from groq import Groq
import threading
import time

# Function to ensure pip is installed
def ensure_pip_installed():
    try:
        import pip
    except ImportError:
        print("Pip not found. Installing pip...")
        subprocess.check_call([sys.executable, "-m", "ensurepip", "--upgrade"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

# Function to install required packages
def install_requirements():
    required_packages = ['flask', 'groq']
    for package in required_packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Ensure pip and required packages are installed
ensure_pip_installed()
install_requirements()

app = Flask(__name__)

# Initialize Groq client with your API key
client = Groq(api_key="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")  # Replace with your actual API key

# Function to get a response from Groq API
def get_groq_response(user_input):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def chatbot_response():
    user_input = request.form['msg']
    bot_response = get_groq_response(user_input)
    return jsonify({'response': bot_response})

def open_browser():
    """Open the default web browser to the Flask application."""
    time.sleep(1)  # Short delay to ensure the server is ready before opening the browser
    webbrowser.open('http://127.0.0.1:5000/')

if __name__ == '__main__':
    # Open the web browser in a separate thread
    threading.Thread(target=open_browser).start()
    # Run the Flask app
    app.run(debug=True)
