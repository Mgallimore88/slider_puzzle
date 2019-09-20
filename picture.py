# from p5 import PImage, image, load_image, size
from copy import copy
from p5 import *


class Picture:
    def __init__(self, x_tiles, y_tiles):
        self.original = load_image("mantisshrimp.jpg")
        self.original.load_pixels()
        self.x_tiles = x_tiles
        self.y_tiles = y_tiles
        self.tiles = []
        self.width = self.original.width - self.original.width % self.x_tiles
        self.height = self.original.height - self.original.height % self.y_tiles
        self.tile_width = int(self.width / self.x_tiles)
        self.tile_height = int(self.height / self.y_tiles)
        self.tile_dictionary = {}

    def draw(self, cells):
        image(self.original, (0, 0))

        for x in range(self.x_tiles):
            for y in range(self.y_tiles):
                index = x + y * self.x_tiles
                board_location = (x, y)
                tile = cells[index]
                self.display_tile(board_location, tile)

    def display_tile(self, board_location, tile):
        x_pos = self.tile_width * board_location[0]
        y_pos = self.tile_height * board_location[1]
        if tile == None:
            image(self.tile_dictionary[-1, -1], (x_pos, y_pos))
        else:
            image(self.tile_dictionary[tile], (x_pos, y_pos))

    def create_canvas(self):
        size(self.width, self.height)

    def new_tile(self, x_loc, y_loc, tile_width, tile_height):
        tile = PImage(tile_width, tile_height)
        tile.load_pixels()
        x_offset = x_loc * tile_width
        y_offset = y_loc * tile_height

        print("------initializing tiles--------")
        print(f"x_location {x_loc}")
        print(f"y_location {y_loc}")
        print(f"x_offset {x_offset}")
        print(f"y_offset {y_offset}")
        print(f"parent image {self.original.width} x {self.original.height}")
        print(f"window {self.width} x {self.height}")

        for x in range(tile_width):
            for y in range(tile_height):
                tile[x, y] = self.original[x + x_offset, y + y_offset]
        return tile

    def make_tiles(self):
        for x in range(self.x_tiles):
            for y in range(self.y_tiles):
                new_tile = self.new_tile(x, y, self.tile_width, self.tile_height)
                self.tiles.append(new_tile)
        self.tiles.append(self.empty_tile())
        self.make_tile_dictionary()
        return self.tiles

    def empty_tile(self):
        empty_tile = PImage(self.tile_width, self.tile_height)
        empty_tile.load_pixels()
        for x in range(self.tile_width):
            for y in range(self.tile_height):
                empty_tile[x, y] = 0
        return empty_tile

    def make_tile_dictionary(self):
        for x in range(self.x_tiles):
            for y in range(self.y_tiles):
                index = x + y * self.x_tiles
                self.tile_dictionary[(x, y)] = self.tiles[index]
        self.tile_dictionary[(-1, -1)] = self.tiles[-1]
        print(self.tile_dictionary)
