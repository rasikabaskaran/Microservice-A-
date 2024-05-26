## High-Contrast Background Color Pairs Microservice 

## Overview 
This microservice provides functionality for generating high-contrast color pairs and dynamically adjusting them based on ambient light conditions. 

## Files
- **server.py**: This file contains the Flask-based server program that implements the microservice. It listens for incoming HTTP requests and responds with high-contrast color pairs.
- **index.html**: The HTML file that serves as the frontend interface for interacting with the microservice. It includes buttons to trigger color changes.
- **styles.css**: The stylesheet for the frontend, defining the aesthetics and layout of the HTML page.
- **app.js**: The JavaScript file that handles the logic for making requests to the server and updating the webpage based on the received responses.

## How to Programmatically REQUEST Data
To request data from the microservice, simply interact with the web interface provided by the HTML file. Follow these steps:

### 1. Start the Microservice Server
Navigate to the directory containing the microservice files and run the server script by executing:
```bash
python server.py
```
This will start the Flask server, making the microservice available at `http://localhost:5000/`.

### 2. Open the Web Interface
Open a web browser and go to `http://127.0.0.1:5000/`. This will load the HTML page that interfaces with the microservice.

### 3. Use the Interface
Click the "Light Mode" and "Dark Mode" buttons on the webpage to send requests to the microservice. The page will display high-contrast color pairs based on your selection.

## How to Programmatically RECEIVE Data
The server processes requests as follows:

### Process Requests
When a user clicks a button on the web interface (`index.html`), a request is sent to `/get_contrast_colors` with a specified mode (`light` or `dark`). The server processes this request and returns the appropriate color scheme.

## Example Interaction
Here's a simplified overview of how the interaction occurs:

1. **User clicks "Dark Mode"** on the webpage.
2. **JavaScript makes an HTTP GET request** to the server with the query parameter `?mode=dark`.
3. **Server processes the request**, determining the appropriate high-contrast colors.
4. **Server sends a JSON response** with the colors `{ text_color: "#FFFFFF", background_color: "#000000" }`.
5. **JavaScript updates the webpage's styles** to reflect the new color scheme.

## Next Steps
- For further customization, users can modify `styles.css` to alter the appearance or add more functionality in `app.js` to handle additional interaction patterns.
- Consider adding more features like user-defined color schemes or integration with real-time lighting data for ambient adjustments.

