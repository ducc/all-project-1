from Board import Board
from Game import Game

board = Board()
players = ['X', 'O']

game = Game(board, players)
game.start()
