"""Runs the game client"""

# importing the Board and Game classes from submodules
from board import Board
from game import Game

# instantiating a new Board object
BOARD = Board()

# defining the player icons
PLAYERS = ['X', 'O']

# instantiating a new Game object with the BOARD instance and PLAYERS as parameters
GAME = Game(BOARD, PLAYERS)

# starting the game
GAME.start()
