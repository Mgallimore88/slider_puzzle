from p5 import size, background
from board import Board
from picture import Picture


class SketchManager:
    def __init__(self):
        self.num_cols = 4
        self.num_rows = 4
        self.board = Board(self.num_rows, self.num_cols)
        self.picture = Picture(self.num_rows, self.num_cols)

    def setup(self):
        self.picture.create_canvas()
        self.picture.make_tiles()
        background(100)

    def draw(self):
        self.picture.draw(self.board.cells)


    def key_pressed(self, event):
        if event.key == "UP":
            self.board.move("UP")
            print(f'cells{self.board.cells}')

        if event.key == "DOWN":
            self.board.move("DOWN")
            print(f'cells{self.board.cells}')

        if event.key == "LEFT":
            self.board.move("LEFT")

        if event.key == "RIGHT":
            self.board.move("RIGHT")

        self.board.print()
