class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.tiles = [0] * rows * cols
        self.populate()
        self.set_empty_tile(0, 0)

    def populate(self):
        for x in range(self.rows):
            for y in range(self.cols):
                self.tiles[x + y * self.rows] = (x, y)
    
    def print(self):
        print ("-------")
        for n in range(self.rows):
            start_index = n * self.cols
            end_index = start_index + self.rows
            print(self.tiles[start_index : end_index])
        print ("-------")


    def get_tile(self, row, col):
        tile_contents = self.tiles[row + col * self.rows]
        return tile_contents

    def set_tile(self, row, col, tile_contents):
        self.tiles[row + col * self.rows] = tile_contents

    def set_empty_tile(self, row, col):
        self.set_tile(row, col, None)

    def get_empty_tile(self):
        for x in range(self.rows):
            for y in range(self.cols):
                if self.get_tile(x, y) == None:
                    return (x, y)

    def swap(self, x1, y1, x2, y2):
        tile_1 = self.get_tile(x1, y1)
        tile_2 = self.get_tile(x2, y2)
        self.set_tile(x1, y1, tile_2)
        self.set_tile(x2, y2, tile_1)

    def move(self, direction):
        empty_tile = self.get_empty_tile()
        empty_x = empty_tile[0]
        empty_y = empty_tile[1]

        if direction == "UP":
            if empty_y == self.rows - 1:
                return
            self.swap(empty_x, empty_y, empty_x, empty_y + 1)

        elif direction == "DOWN":
            if empty_y == 0:
                return
            self.swap(empty_x, empty_y, empty_x, empty_y - 1)

        elif direction == "LEFT":
            if empty_x == self.cols - 1:
                return
            self.swap(empty_x, empty_y, empty_x + 1, empty_y)

        elif direction == "RIGHT":
            if empty_x == 0:
                return
            self.swap(empty_x, empty_y, empty_x - 1, empty_y)
