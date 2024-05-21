import zmq

def request_color_pairs():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5679")
    socket.send_pyobj({"request": "generate_pairs"})
    response = socket.recv_pyobj()
    return response

def request_adjusted_color_pair(light_level):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5679")
    socket.send_pyobj({"request": "adjust_for_light", "light_level": light_level})
    adjusted_pair = socket.recv_pyobj()
    return adjusted_pair

def main():
    print("Requesting high-contrast color pairs...")
    pairs = request_color_pairs()
    print("Received high-contrast color pairs:", pairs)

    print("\nRequesting color adjustment for low light conditions...")
    adjusted_pair = request_adjusted_color_pair(30)
    print("Adjusted color pair for low light:", adjusted_pair)

if __name__ == "__main__":
    main()


