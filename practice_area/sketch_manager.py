from p5 import size, background
from copy import copy, deepcopy
import vispy
import numpy
from p5 import *


class SketchManager:
    def __init__(self):
        self.my_image = load_image("mantisshrimp.jpg")
        self.my_image.load_pixels()
        self.new_tile = PImage(200, 200)
        self.new_tile.load_pixels()
        self.centre_area = PImage(200, 200)
        self.centre_area.load_pixels()
        self.x = 0
        self.y = 0
        # modify the parent image with a black square
        for x in range(100):
            for y in range(100):
                self.my_image[x, y] = 0
        # smaller PImage object using pixels from the parent image
        for x in range(200):
            for y in range(200):
                self.new_tile[x, y] = self.my_image[x, y]

        # portion of pixels from a different origin on the parent image
        for x in range(200):
            for y in range(200):
                self.centre_area[x, y] = self.my_image[x + 200, y]

    def setup(self):
        size(self.my_image.size[0], self.my_image.size[1])

    def draw(self):
        background(self.my_image)

        image(self.new_tile, (mouse_x, mouse_y))
        image(self.new_tile, (300, 100))
        image(self.centre_area, (0, 300))

        # moves
        self.x += 1
        image(self.centre_area, (self.x, self.y))

    def key_pressed(self, event):
        self.x = mouse_x
        self.y = mouse_y
