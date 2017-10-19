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