# from p5 import PImage, image, load_image, size
from copy import copy
from p5 import *


class Picture:
    def __init__(self, x_tiles, y_tiles):
        self.original = load_image("mantisshrimp.jpg")
        self.x_tiles = x_tiles
        self.y_tiles = y_tiles
        self.tile = PImage(100,100)



    def draw(self):
        image(self.original, (0, 0))

    def create_canvas(self):
        width = self.original.width - self.original.width % self.x_tiles
        height = self.original.height - self.original.height % self.y_tiles
        size(width, height)

    def make_tile(self, x_index = 0, y_index = 0):
        for x in range(100):
            for y in range(100):
                index = x+ y*width
                test = self.original._get_pixel[index]
                self.tile._set_pixel(test.key, test.point)
                
            
                
                


        print(test)
        print(test2)





        
