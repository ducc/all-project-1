"""Handles the running of tic-tac-toe games"""

import checks


class Game:
    """Represents a game of tic-tac-toe"""

    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.current_player = 0
        self.playing = True

    def get_player(self):
        """Returns the current player's symbol"""

        return self.players[self.current_player]

    def __ask_for_tile(self):
        user_input = input("player " + self.get_player() + ":\n")

        if user_input == "exit":
            return None

        try:
            return int(user_input)
        except ValueError:
            print("invalid input - integer or exit")
            return self.__ask_for_tile()

    def __choose_next_player(self):
        if (self.current_player < len(self.players) - 1):
            self.current_player += 1
        else:
            self.current_player = 0

    def __check_if_won(self):
        iterations = self.board.SIZE - 1
        board = self.board.tiles

        # check vertical wins
        for j in range(iterations):
            if checks.check_win_vertical(board, j):
                return True
        
        # check horizontal wins
        for i in range(iterations):
            if checks.check_win_horizontal(board, i):
                return True

        # check diagonal wins
        if checks.check_win_diagonal_lr(board):
            return True

        if checks.check_win_diagonal_rl(board):
            return True

    def start(self):
        """Begins the tic-tac-toe game"""

        board_size = self.board.SIZE
        
        while True:
            chosen_tile = self.__ask_for_tile()

            if chosen_tile is None:
                break

            while chosen_tile < 1 or chosen_tile > board_size * board_size:
                print("tile is out of bounds!")
                chosen_tile = self.__ask_for_tile()

            player = self.get_player()
            self.board.set_tile(chosen_tile - 1, player)
            
            self.board.clear()
            self.board.draw()

            if self.__check_if_won():
                print("Player " + player + " won!")
                break
            
            self.__choose_next_player()