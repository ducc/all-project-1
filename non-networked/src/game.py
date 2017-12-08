"""Handles the running of tic-tac-toe games"""

# importing the checks module for win checking
import checks


# this class is for the running of the game. it handles the game logic as well as using the board module to render the game board. 
class Game:
    """Represents a game of tic-tac-toe"""

    # a constructor that takes a Board instance and a list of player characters for showing which player has claimed a tile on the board
    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.current_player = 0 

    # players are represented as integers for the game logic so this function is required to display players as symbols from the players list
    def get_player(self):
        """Returns the current player's symbol"""

        return self.players[self.current_player]

    # waits for the current player to input the tile they want to play next
    # returns the tile as an integer or None if the player wishes to exit the game
    def __ask_for_tile(self):
        user_input = input("player " + self.get_player() + ":\n")

        # if the user inputted "exit" return None to stop the game
        if user_input == "exit":
            return None

        # here we are using a try/except block to catch invalid inputs
        try:
            return int(user_input)
        except ValueError:
            # output that the user has made an error in their input and reccursively ask for input again
            print("invalid input - integer or exit")
            return self.__ask_for_tile()

    # determines the next player in the game written in a way that could be expanded in the future for larger board grids
    def __choose_next_player(self):
        if (self.current_player < len(self.players) - 1):
            self.current_player += 1
        else:
            self.current_player = 0

    # checks if there has been a win on the board with a 3-in-a-row of the same tile values using the checks module
    # returns True if there has been a win
    def __check_if_won(self):
        iterations = self.board.SIZE - 1

        # alias variable to keep code clean
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

    # starts the game
    def start(self):
        """Begins the tic-tac-toe game"""

        board_size = self.board.SIZE
        
        # a never ending loop for the game logic
        while True:
            # get the next tile to choose
            chosen_tile = self.__ask_for_tile()

            # __ask_for_tile returns None if the game should exit
            # if this is the case the loop is broken out of
            if chosen_tile is None:
                break

            # checks that the inputted tile is within the size of the board
            while chosen_tile < 1 or chosen_tile > board_size * board_size:
                print("tile is out of bounds!")
                # if the tile is out of bounds request a new input
                chosen_tile = self.__ask_for_tile()

            # sets the chosen tile to the player's icon
            player = self.get_player()
            self.board.set_tile(chosen_tile - 1, player)
            
            # clear the old board and redraw
            self.board.clear()
            self.board.draw()

            # if the game has been one, announce the winner and exit the game
            if self.__check_if_won():
                print("Player " + player + " won!")
                break
            
            # choose the next player for the game and continue 
            self.__choose_next_player()
