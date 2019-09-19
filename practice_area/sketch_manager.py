
from p5 import size, background
from p5 import *


class SketchManager:
    def __init__(self):
        self.my_image = PImage(20, 20)
        self.new_tile = PImage(100,100)
        self.my_image = load_image("mantisshrimp.jpg")
        self.new_tile = load_image("mantisshrimp.jpg")
        self.new_tile.size = (200,200)

        
        

    def setup(self):
        size(self.my_image.size[0], self.my_image.size[1])
        background(self.my_image)
        for x in range(100):
            for y in range(100):
                self.my_image[x, y] = 0

        self.colours = []

        for x in range(20):
            for y in range(20):
                index = x + y * 20
                self.colours.append(self.my_image[x,y])

        

                

    def draw(self):
        image(self.my_image, (mouse_x, mouse_y))
        image(self.new_tile, (300,300))
        pass