from flask import Flask, jsonify, request, render_template
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_contrast_colors')
def get_contrast_colors():
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
    app.run(debug=True, port=5000)
