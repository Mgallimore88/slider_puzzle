# from p5 import PImage, image, load_image, size
from copy import copy
from p5 import *


class Picture:
    def __init__(self, num_cols, num_rows):
        self.original = load_image("mantisshrimp.jpg")
        self.original.load_pixels()
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.tiles = []
        self.width = self.original.width - self.original.width % self.num_cols
        self.height = self.original.height - self.original.height % self.num_rows
        self.tile_width = int(self.width / self.num_cols)
        self.tile_height = int(self.height / self.num_rows)

    def draw(self, cells):
        image(self.original, (0, 0))

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                board_location = (row, col)
                tile = cells[row][col]
                self.display_tile(board_location, tile)

    def display_tile(self, board_location, tile):
        x_pos = self.tile_width * board_location[1]
        y_pos = self.tile_height * board_location[0]
        if tile == None:
            image(self.tiles[0][0], (x_pos, y_pos))
        else:
            row, col = tile
            image(self.tiles[row][col], (x_pos, y_pos))

    def create_canvas(self):
        size(self.width, self.height)

    def new_tile(self, y_idx, x_idx, tile_width, tile_height):
        tile = PImage(tile_width, tile_height)
        tile.load_pixels()
        x_offset = x_idx * tile_width
        y_offset = y_idx * tile_height

        print("------initializing tiles--------")
        print(f"tile {x_idx}, {y_idx}")

        for y in range(tile_height):
            for x in range(tile_width):
                tile[x, y] = self.original[x + x_offset, y + y_offset]
        return tile

    def make_tiles(self):
        # get a tile for each position on the grid
        for row in range(self.num_rows):
            self.tiles.append([self.new_tile(row, col, self.tile_width, self.tile_height) for col in range(self.num_cols)])
        # put a black tile in the first position in the list.
        self.tiles[0][0] = self.empty_tile()
        return self.tiles

    def empty_tile(self):
        empty_tile = PImage(self.tile_width, self.tile_height)
        empty_tile.load_pixels()
        for x in range(self.tile_width):
            for y in range(self.tile_height):
                empty_tile[x, y] = 0
        return empty_tile
