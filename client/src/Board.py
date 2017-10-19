import os


class Board:
    SIZE = 3

    def __init__(self):
        self.tiles = [[""] * self.SIZE for i in range(self.SIZE)]
        self.__create_labels()
        self.draw()

    def __create_labels(self):
        counter = 0
        
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                counter += 1
                self.tiles[i][j] = counter

    def __print_devider(self):
        print('|'.join(['____' for x in range(self.SIZE)]))

    def __print_blank(self):
        print('|'.join(['    ' for x in range(self.SIZE)]))

    def __print_labels(self, counter):
        row = ' | '.join(['%2s' % self.tiles[counter][x] for x in range(self.SIZE)])
        row = ' ' + row
        print(row)

    def draw(self):
        """Renders the board"""

        for i in range(self.SIZE):
            self.__print_blank()
            self.__print_labels(i)

            if (i == self.SIZE - 1):
                self.__print_blank()
            else:
                self.__print_devider()

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