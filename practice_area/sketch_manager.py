from p5 import size, background
from p5 import *


class SketchManager:
    def __init__(self):
        self.my_image = PImage(20, 20)
        self.my_image = load_image("mantisshrimp.jpg")

    def setup(self):
        size(self.my_image.size[0], self.my_image.size[1])
        background(self.my_image)
        pixels = load_pixels()
        print(f"pixels {pixels}")
        print(self.my_image)
        for x in range(100):
            for y in range(100):
                self.my_image[x, y] = 0

    def draw(self):
        image(self.my_image, (mouse_x, mouse_y))
        pass
