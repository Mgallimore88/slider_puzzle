from random import randint


class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = [0] * rows * cols
        self.populate()
        self.set_empty_cell(0, 0)

    def populate(self):
        for x in range(self.rows):
            for y in range(self.cols):
                self.cells[x + y * self.rows] = (x, y)

    def print(self):
        print("-------")
        for n in range(self.rows):
            start_index = n * self.cols
            end_index = start_index + self.rows
            print(self.cells[start_index:end_index])
        print("-------")

    def get_cell(self, row, col):
        cell_contents = self.cells[row + col * self.rows]
        return cell_contents

    def set_cell(self, row, col, cell_contents):
        self.cells[row + col * self.rows] = cell_contents

    def set_empty_cell(self, row, col):
        self.set_cell(row, col, None)

    def get_empty_cell(self):
        for x in range(self.rows):
            for y in range(self.cols):
                if self.get_cell(x, y) == None:
                    return (x, y)

    def swap(self, x1, y1, x2, y2):
        cell_1 = self.get_cell(x1, y1)
        cell_2 = self.get_cell(x2, y2)
        self.set_cell(x1, y1, cell_2)
        self.set_cell(x2, y2, cell_1)

    def move(self, direction):
        empty_cell = self.get_empty_cell()
        empty_x = empty_cell[0]
        empty_y = empty_cell[1]

        if direction == "UP":
            if empty_y == self.rows - 1:
                return
            self.swap(empty_x, empty_y, empty_x, empty_y + 1)

        elif direction == "DOWN":
            if empty_y == 0:
                return
            self.swap(empty_x, empty_y, empty_x, empty_y - 1)

        elif direction == "LEFT":
            if empty_x == self.cols - 1:
                return
            self.swap(empty_x, empty_y, empty_x + 1, empty_y)

        elif direction == "RIGHT":
            if empty_x == 0:
                return
            self.swap(empty_x, empty_y, empty_x - 1, empty_y)

    def scramble(self, num_of_moves):
        dice = {1: "UP", 2: "DOWN", 3: "LEFT", 4: "RIGHT"}
        for n in range(num_of_moves):
            roll = randint(1, 4)
            self.move(dice[roll])
