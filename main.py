from p5 import *
from board import Board
from sketch_manager import SketchManager

global sketch
sketch = SketchManager()


def setup():
    sketch.setup()


def draw():
    sketch.draw()


def key_pressed(event):
    sketch.key_pressed(event)


run()
