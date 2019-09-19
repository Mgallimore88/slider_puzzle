
from p5 import size, background
from copy import copy, deepcopy
import vispy
import numpy
from p5 import *


class SketchManager:
    def __init__(self):
        self.my_image = load_image("mantisshrimp.jpg")
        self.new_tile = load_image("mantisshrimp.jpg")
        self.new_tile.load_pixels()
        self.new_tile.size = (200,200)
        self.colours = []

        
        

    def setup(self):
        size(self.my_image.size[0], self.my_image.size[1])
        background(self.my_image)
        for x in range(100):
            for y in range(100):
                self.my_image[x, y] = 0
        for x in range(50):
            for y in range(50):
                self.new_tile[x, y] = 0
                # index = x + y * 150
                # self.colours.append(self.my_image[x,y])

    def draw(self):
        image(self.my_image, (mouse_x, mouse_y))
        image(self.new_tile, (300,300))
        pass