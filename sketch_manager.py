from p5 import size, background
from board import Board


class SketchManager:
    def __init__(self):
        self.board = Board(4, 4)

    def setup(self):
        size(200, 200)
        background(100)

    def draw(self):
        pass

    def key_pressed(self, event):
        if event.key == 'UP':
            self.board.move('UP')
            
        if event.key == 'DOWN':
            self.board.move('DOWN')

        if event.key == 'LEFT':
            self.board.move('LEFT')

        if event.key == 'RIGHT':
            self.board.move('RIGHT')
        
        self.board.print()

