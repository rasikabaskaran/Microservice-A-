from flask import Flask, jsonify, request
from flask_cors import CORS 
import zmq

app = Flask(__name__)
CORS(app)

# ZeroMQ setup
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

@app.route('/get_contrast_colors')
def get_contrast_colors():
    """
    Endpoint to retrieve color contrast pairs based on the specified mode.
    If no mode is provided, the default mode is 'dark'.
    Returns:
        JSON object containing text_color and background_color.
    """
    mode = request.args.get('mode', 'dark')  # Default mode is 'dark'

    if mode == 'light':
        colors = {
            'text_color': '#000000',  # Black text
            'background_color': '#FFFFFF'  # White background
        }
    else:
        colors = {
            'text_color': '#FFFFFF',  # White text
            'background_color': '#000000'  # Black background
        }

    return jsonify(colors)

if __name__ == '__main__':
    while True:
        # Wait for request from client
        message = socket.recv_string()
        action, *args = message.split(",")

        # Perform requested action
        if action == 'get_contrast_colors':
            mode = args[0] if args else 'dark'  # Default mode is 'dark'

            if mode == 'light':
                colors = {
                    'text_color': '#000000',  # Black text
                    'background_color': '#FFFFFF'  # White background
                }
            else:
                colors = {
                    'text_color': '#FFFFFF',  # White text
                    'background_color': '#000000'  # Black background
                }
                
            socket.send_json(colors)

        else:
            socket.send_string("Invalid action")
