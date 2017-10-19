from os import system
from os import name as osname


class Board:
    SIZE = 3

    def __init__(self):
        self.tiles = [[""] * self.SIZE for i in range(self.SIZE)]
        self.create_labels()
        self.draw()

    def create_labels(self):
        counter = 0
        
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                counter += 1
                self.tiles[i][j] = counter

    def print_devider(self):
        print('|'.join(['____' for x in range(self.SIZE)]))

    def print_blank(self):
        print('|'.join(['    ' for x in range(self.SIZE)]))

    def print_labels(self, counter):
        row = ' | '.join(['%2s' % self.tiles[counter][x] for x in range(self.SIZE)])
        row = ' ' + row
        print(row)

    def draw(self):
        for i in range(self.SIZE):
            self.print_blank()
            self.print_labels(i)

            if (i == self.SIZE - 1):
                self.print_blank()
            else:
                self.print_devider()

    def clear(self):
        if osname is "nt": # check if the os is windows
            system("cls")
        else:
            system("clear")

    def set_tile(self, tile, value):
        self.tiles[tile // self.SIZE][tile % self.SIZE] = value