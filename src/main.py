from Board import Board
from Game import Game

board = Board(3)
players = ['X', 'O']

game = Game(board, players)
game.start()
