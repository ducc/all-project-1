from os import system
from os import name as osname


class Board:
    def __init__(self, size):
        self.size = size
        self.tiles = [[""] * size for i in range(size)]
        self.create_labels()
        self.draw()

    def create_labels(self):
        counter = 0
        
        for i in range(self.size):
            for j in range(self.size):
                counter += 1
                self.tiles[i][j] = counter

    def print_devider(self):
        print('|'.join(['____' for x in range(self.size)]))

    def print_blank(self):
        print('|'.join(['    ' for x in range(self.size)]))

    def print_labels(self, counter):
        row = ' | '.join(['%2s' % self.tiles[counter][x] for x in range(self.size)])
        row = ' ' + row
        print(row)

    def draw(self):
        for i in range(self.size):
            self.print_blank()
            self.print_labels(i)

            if (i == self.size - 1):
                self.print_blank()
            else:
                self.print_devider()

    def clear(self):
        if osname == "nt": # check if the os is windows
            system("cls")
        else:
            system("clear")

    def set_tile(self, tile, value):
        self.tiles[tile // self.size][tile % self.size] = value


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
        board = self.board.tiles

    def start(self):
        board_size = self.board.size
        
        while True:
            chosen_tile = self.ask_for_tile()

            if chosen_tile == None:
                break

            while chosen_tile < 1 or chosen_tile > board_size * board_size:
                print("tile is out of bounds!")
                chosen_tile = self.ask_for_tile()

            self.board.set_tile(chosen_tile - 1, self.players[self.current_player])
            
            self.board.clear()
            self.board.draw()
            
            self.choose_next_player()


board = Board(3)
players = ['X', 'O']

game = Game(board, players)
game.start()
