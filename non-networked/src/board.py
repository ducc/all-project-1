"""Handles the "screen" of a game"""

# importing the os library for running the terminal clear commands
import os


# this class handles the board rendering and the tiles on the board which players choose to make moves on the game
class Board:
    """Represents a tic-tac-toe board"""

    # this is the constant size of the board which produces a 3x3 grid
    SIZE = 3

    # the code inside this constructor populates the tiles list with blank tiles
    def __init__(self):
        # populating the tiles grid
        self.tiles = [[""] * self.SIZE for i in range(self.SIZE)]
        # setting the tile labels to their default values
        self.__create_labels()
        # rendering the grid onto the terminal
        self.draw()

    # this method sets each tile in the grid to numbers from 1 to 9
    def __create_labels(self):
        counter = 0
        
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                counter += 1 # incrementing the tile number counter
                self.tiles[i][j] = counter # assigning a number to the tile

    # draws deviders for the tiles on the grid
    def __print_devider(self):
        print('|'.join(['____' for x in range(self.SIZE)]))

    # draws blanks for padding around the tiles
    def __print_blank(self):
        print('|'.join(['    ' for x in range(self.SIZE)]))

    # prints each row of the grid with tile numbers
    def __print_labels(self, counter):
        row = ' | '.join(['%2s' % self.tiles[counter][x] for x in range(self.SIZE)])
        row = ' ' + row
        print(row)

    # renders the board using the 3 methods defined above
    def draw(self):
        """Renders the board"""

        # iterating over the size of the grid to draw the board
        for i in range(self.SIZE):
            self.__print_blank()
            self.__print_labels(i)

            if (i == self.SIZE - 1):
                self.__print_blank()
            else:
                self.__print_devider()

    # clears the terminal using system commands
    def clear(self):
        """Clears the screen ready for the board to be drawn again"""

        # command to clear the screen is different depending on the OS
        if os.name is "nt": # check if the os is windows
            os.system("cls")
        else: # clear is used on most unix based systems
            os.system("clear")

    def set_tile(self, tile, value):
        """Sets the label of the specified tile"""

        self.tiles[tile // self.SIZE][tile % self.SIZE] = value

