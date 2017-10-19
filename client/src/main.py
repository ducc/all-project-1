"""Runs the game client"""

from board import Board
from game import Game

BOARD = Board()
PLAYERS = ['X', 'O']

GAME = Game(BOARD, PLAYERS)
GAME.start()
