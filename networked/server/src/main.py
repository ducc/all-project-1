from dotenv import load_dotenv, find_dotenv
import os, socket, io, select, protocol
from protocol import OPCODES, get_opcode

# load .env configuration into our environment variables
load_dotenv(find_dotenv())

# server port to bind to
PORT = int(os.environ.get("TICTACTOE_PORT"))

# initializing the socket server and binding to the port
sock = socket.socket()
sock.bind(("", PORT))

# listen for a new client connection with a maximum queued connections of 5
sock.listen(5)

print("server running on port {}".format(PORT))

# list of connected clients
clients = []

# list of players stored in a (conn, player) tuple
players = []

current_player = "X"

def get_player_by_conn(conn):
    for (c, player) in players:
        if c is conn:
            return player

    return None

def get_conn_by_player(player):
    ...

def poll():
    read, write, error = select.select(clients+[sock], clients, clients, 0)

    for conn in read:
        if conn is sock: # new client
            c, addr = sock.accept()
            clients.append(c)

            player = "X"
            if len(players) == 1:
                player = "O"

            players.append((c, player))

            print("player {} connected!\naddr: {}\nconnected: {}"
                    .format(player, addr, len(players)))

            message = protocol.NameMessage(player)
            c.send(message.buffer)

            if len(players) == 2:
                message = protocol.ReadyMessage()
                clients[0].send(message.buffer)
        else:
            raw = conn.recv(1024)
            player = get_player_by_conn(conn)

            if not raw:
                continue
 
            print("msg from player {}".format(player))

            buf = bytearray(raw)
            reader = io.BytesIO(buf)

            opcode = protocol.Message.decode(reader).opcode
            opcode_name = OPCODES[opcode]

            print("recv msg opcode {}".format(opcode_name))

            if opcode_name == "SEND_MOVE":
                tile = protocol.SendMoveMessage.decode(reader).tile
                print("moving tile {}!", tile)

                
            elif opcode_name == "SEND_QUIT":
                print("oh no the client wants to quit")

            reader.close()

try:
    while True:
        poll()

except KeyboardInterrupt:
    pass

finally:
    for c in clients:
        c.close()

    sock.shutdown(1)
    sock.close()
    print("shutdown")


