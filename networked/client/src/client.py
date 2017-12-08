from dotenv import load_dotenv, find_dotenv
import os, socket, io, protocol
from protocol import get_opcode, OPCODES
from board import Board
from game import Game

# load .env configuration into our environment variables
load_dotenv(find_dotenv())

# server host & port to connect to
HOST = os.environ.get("TICTACTOE_HOST")
PORT = int(os.environ.get("TICTACTOE_PORT"))

# initializing the socket client and binding to the port
sock = socket.socket()
sock.connect((HOST, PORT))

print("connected to {}:{}".format(HOST, PORT))

PLAYERS = ["X", "O"]

# setup the game
board = Board()
game = Game(board, PLAYERS)

board_size = board.SIZE

player_name = "unknown"

try:
    while True:
        raw = sock.recv(1024)

        if not raw:
            print("disconnected")
            break

        reader = io.BytesIO(raw)
        opcode = protocol.Message.decode(reader).opcode
        opcode_name = OPCODES[opcode]

        if opcode_name == "NAME":
            name = protocol.NameMessage.decode(reader).name
            player_name = name
            print("assigned name {}", player_name)
        elif opcode_name == "READY":
            chosen_tile = game.ask_for_tile()
            if chosen_tile == None:
                break

            while chosen_tile < 1 or chosen_tile > board_size * board_size:
                print("tile is out of bounds!")
                chosen_tile = game.ask_for_tile()

            board.set_tile(chosen_tile - 1, PLAYERS[game.current_player]) 
            board.clear()
            board.draw()

            message = protocol.SendMoveMessage(chosen_tile)
            sock.send(message.buffer)

            if game.check_if_won():
                print("Player " + PLAYERS[game.current_player] + " won!")
                message = protocol.SendQuitMessage()
                sock.send(message.buffer)
                break

            game.current_player = game.choose_next_player()
        elif opcode_name == "RECV_MOVE":
            chosen_tile = protocol.RecvMoveMessage.decode(reader).tile
            print("player moved tile {}", chosen_tile)

            board.set_tile(chosen_tile - 1, PLAYERS[game.current_player])
            board.clear()
            board.draw()

            if game.check_if_won():
                print("Player " + PLAYERS[game.current_player] + " won!")
                message = protocol.SendQuitMessage()
                sock.send(message.buffer)
                break

            game.current_player = game.choose_next_player()
            
            chosen_tile = game.ask_for_tile()
            if chosen_tile == None:
                break

            while chosen_tile < 1 or chosen_tile > board_size * board_size:
                print("tile is out of bounds!")
                chosen_tile = game.ask_for_tile()

            board.set_tile(chosen_tile - 1, PLAYERS[game.current_player])
            board.clear()
            board.draw()

            message = protocol.SendMoveMessage(chosen_tile)
            sock.send(message.buffer)

            if game.check_if_won():
                print("Player " + PLAYERS[game.current_player] + " won!")
                message = protocol.SendQuitMessage()
                sock.send(message.buffer)
                break

            game.current_player = game.choose_next_player()
        elif opcode_name == "RECV_QUIT":
            print("the other player quit!")

except KeyboardInterrupt:
    pass

finally:
    sock.shutdown(1)
    sock.close()
