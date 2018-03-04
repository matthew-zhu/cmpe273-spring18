import zmq
import sys
import select

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock_push = context.socket(zmq.PUSH)
sock_push.connect("tcp://127.0.0.1:5678")

sock_sub = context.socket(zmq.SUB)
sock_sub.connect("tcp://127.0.0.1:5679")
sock_sub.setsockopt(zmq.SUBSCRIBE, b'')

# Initialize user
user = sys.argv[1]
print("User[%s] Connected to the chat server." % user)

def user_prompt():
    sys.stdout.write("[%s] > " % user)
    sys.stdout.flush()

user_prompt()
while True:
    # Check for user input; Send to server if input exists
    user_input = select.select([sys.stdin], [], [], 0)[0]
    if user_input:
        msg = user_input[0].readline().split('\n')[0]
        msg = ("[%s]: " % user) + msg
        sock_push.send_string(msg)
        user_prompt()

    # Poll for messages from server
    if sock_sub.poll(1) > 0:
        msg = sock_sub.recv().decode()
        if msg:
            u = msg.split("[",1)[1].split("]",1)[0]
            if u != user:
                print('\n' + msg)
                user_prompt()

