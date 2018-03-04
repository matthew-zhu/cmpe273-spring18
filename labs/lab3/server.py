import zmq

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock_pull = context.socket(zmq.PULL)
sock_pull.bind("tcp://127.0.0.1:5678")

sock_pub = context.socket(zmq.PUB)
sock_pub.bind("tcp://127.0.0.1:5679")

while True:
    # When message is received, publish to all clients
    msg = sock_pull.recv()
    if msg:
        print("[Server] Echo: " + msg.decode())
        sock_pub.send(msg)
