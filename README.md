## High-Contrast Background Color Pairs Microservice 

## Overview 
This microservice provides functionality for generating high-contrast color pairs and dynamically adjusting them based on ambient light conditions. 

## Files
- **server.py:** This file contains the server program that implements the microservice. It listens for incoming requests, processes them based on the type (static or ambient light-adjusted), and sends back the appropriate high-contrast color pairs.
- **client.py:** This file contains the client program that demonstrates how to make requests to the microservice and receive responses. It's useful for testing and can be used as an example for integrating the microservice into other projects.

## How to Programmatically REQUEST Data
To request data from the microservice, follow these steps:

1. **Connect to the Microservice:** Open a terminal window and navigate to the directory containing the microservice files.
2. **Start the Microservice Server:** Run the server script by executing the following command:
   ```bash
   python server.py
   ```
3. **Send Request:** In a separate terminal window, run the client script to send requests and receive responses. Example commands include:
   - **Generate High-Contrast Color Pairs:**
     ```bash
     python client.py generate_pairs
     ```
   - **Adjust Color Based on Ambient Light:**
     ```bash
     python client.py adjust_for_light 50
     ```

## How to Programmatically REQUEST Data
To request data from the microservice, follow these steps:

1. **Connect to the Microservice:** Open a terminal window and navigate to the directory containing the microservice files.
2. **Start the Microservice Server:** Run the server script by executing the following command:
   ```bash
   python server.py
   ```
3. **Send Request:** In a separate terminal window, run the client script to send requests and receive responses. Example commands include:
   - **Generate High-Contrast Color Pairs:**
     ```bash
     python client.py generate_pairs
     ```
   - **Adjust Color Based on Ambient Light:**
     ```bash
     python client.py adjust_for_light 50
     ```

## How to Programmatically RECEIVE Data
To receive requests and send back responses, follow these steps:

1. **Start the Microservice Server:** Open a terminal window, navigate to the directory containing the microservice files, and start the server by executing:
   ```bash
   python server.py
   ```
2. **Process Requests:** As clients send requests specifying the desired operation (e.g., `generate_pairs` or `adjust_for_light`), the server will automatically process them based on the request type and send back the corresponding high-contrast color pairs.

### Example call and Response:
```python
import zmq

# Connect to the ZeroMQ socket
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5578")

# Example request to the microservice for default high-contrast pairs
socket.send_pyobj({"request": "generate_pairs"})
response = socket.recv_pyobj()
print("Response from microservice:", response)
```
