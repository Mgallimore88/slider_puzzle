class Board:
    def __init__(self, rows=4, cols=4):
        self.rows = rows
        self.cols = cols
        self.tiles = [0] * rows * cols
        self.populate()

    def populate(self):
        for x in range(self.rows):
            for y in range(self.cols):
                self.tiles[x + y * self.rows] = (x, y)

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
        tile_1 = self.get_tile(x1,y1)
        tile_2 = self.get_tile(x2, y2)
        self.set_tile(x1, y1, tile_2)
        self.set_tile(x2, y2, tile_1)


    def move(self, direction = 0):
        empty_tile = self.get_empty_tile()
        empty_x = empty_tile[0]
        empty_y = empty_tile[1]

        if direction == 'UP':
            try:
                self.swap(empty_x, empty_y, empty_x, empty_y + 1)
            except:
                print("invalid move")

        

        elif direction == 'DOWN':
            try:
                self.swap(empty_x, empty_y, empty_x, empty_y - 1)


        elif direction == 'LEFT':
            try:
                self.swap(empty_x, empty_y, empty_x + 1, empty_y)


        elif direction == 'RIGHT': 
            try:
                self.swap(empty_x, empty_y, empty_x - 1, empty_y)



board = Board()
board.populate()
board.set_empty_tile(2, 0)
print(f'getempty{board.get_empty_tile()}')
print(f' post get empty{board.tiles}')

