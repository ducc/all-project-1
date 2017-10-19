from Board import Board
from Game import Game

BOARD = Board()
PLAYERS = ['X', 'O']

GAME = Game(BOARD, PLAYERS)
GAME.start()
