import checks

class Game:
    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.current_player = 0
        self.playing = True

    def ask_for_tile(self):
        user_input = input("player " + str(self.current_player + 1) + ":\n")

        if user_input == "exit":
            return None

        try:
            return int(user_input)
        except ValueError:
            print("invalid input - integer or exit")
            return self.ask_for_tile()

    def choose_next_player(self):
        if (self.current_player < len(self.players) - 1):
            self.current_player += 1
        else:
            self.current_player = 0

    def check_if_won(self):
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

    def start(self):
        board_size = self.board.SIZE
        
        while True:
            chosen_tile = self.ask_for_tile()

            if chosen_tile is None:
                break

            while chosen_tile < 1 or chosen_tile > board_size * board_size:
                print("tile is out of bounds!")
                chosen_tile = self.ask_for_tile()

            self.board.set_tile(chosen_tile - 1, self.players[self.current_player])
            
            self.board.clear()
            self.board.draw()

            if self.check_if_won():
                print("you won!! :)")
                break
            
            self.choose_next_player()