import zmq

def generate_contrast_pairs():
    return [("black", "white"), ("white", "black")]

def adjust_color_pair_for_light(light_level):
    return ("white", "black") if light_level < 50 else ("black", "white")

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5679")
    print("Service is running...")

    while True:
        message = socket.recv_pyobj()
        if message.get("request") == "generate_pairs":
            pairs = generate_contrast_pairs()
            socket.send_pyobj(pairs)
        elif message.get("request") == "adjust_for_light":
            light_level = message.get("light_level", 50)
            adjusted_pair = adjust_color_pair_for_light(light_level)
            socket.send_pyobj(adjusted_pair)

if __name__ == "__main__":
    main()


