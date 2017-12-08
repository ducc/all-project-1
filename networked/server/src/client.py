from dotenv import load_dotenv, find_dotenv
import os, socket, io
from protocol import get_opcode

# load .env configuration into our environment variables
load_dotenv(find_dotenv())

# server host & port to connect to
HOST = os.environ.get("TICTACTOE_HOST")
PORT = int(os.environ.get("TICTACTOE_PORT"))

# initializing the socket client and binding to the port
sock = socket.socket()
sock.connect((HOST, PORT))

print("connected to {}:{}".format(HOST, PORT))

try:
    while True:
        buf = bytearray()
        buf.append(0)
        sock.send(buf)
        break

except: 
    try:
        sock.shutdown(1)
        sock.close()

    except OSError as e:
        if e.errno == 107:
            print("server closed the connection")
        else:
            raise e

