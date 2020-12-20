import copy

f = open("Day20\input2", 'r')
all_tiles = {}
tile_nb = 0
tile = []
for line in f:
    line = line.rstrip("\n")
    if ":" in line:
        tile_nb = int(line.strip("Tile :"))
    elif line == "":
        all_tiles[tile_nb] = tile
        tile = []
    else:
        tile.append(line)
all_tiles[tile_nb] = tile
f.close()

#Part 1
size = 3

class piece:
    def __init__(self, nb, tile):
        self.nb = nb
        self.tile = tile
        self.top = tile[0]
        self.bottom = tile[len(tile)-1]
        self.left = ""
        self.right = ""
        for i in range(len(tile)): 
            self.left += tile[i][0]
            self.right += tile[i][len(tile[0])-1]
        self.rotation = 0
        self.flipped = 0

    def rotate(self):
        self.rotation = (self.rotation+1)%4
        self.top, self.right, self.bottom, self.left = self.left[::-1], self.top, self.right[::-1], self.bottom

    def flip(self):
        self.flipped = (self.flipped+1)%2
        self.top, self.right, self.bottom, self.left = self.top[::-1], self.left, self.bottom[::-1], self.right

    def get_cropped_tile(self):
        print(self.nb, self.rotation, self.flipped)
        cropped = copy.deepcopy(self.tile[1:9])
        for i in range(len(cropped)): cropped[i] = cropped[i][1:9]
        if self.flipped == 1:
            for i in range(len(cropped)): cropped[i] = cropped[i][::-1]
        for r in range(self.rotation):
            new = copy.deepcopy(cropped)
            for i in range(len(new)): new[i] = list(new[i])
            for i in range(len(cropped)):
                for j in range(len(cropped)):
                    new[i][j] = cropped[len(cropped)-1-i][j]
            for i in range(len(new)): new[i] = "".join(new[i])
            cropped = new
        return cropped

def solve_puzzle(used_tiles):
    pieces_nb = len(used_tiles)
    if pieces_nb == len(all_pieces): return True, used_tiles
    for p in all_pieces:
        if p not in used_tiles:
            for r in range(4):
                p.rotate()
                for f in range(2):
                    p.flip()
                    if (pieces_nb%size == 0 or used_tiles[-1].right == p.left) and (pieces_nb//size == 0 or used_tiles[-size].bottom == p.top):
                        print(pieces_nb, used_tiles[-1].right, p.left, p.rotation, p.flipped)
                        result, pieces = solve_puzzle(used_tiles+[p])
                        if result: return True, pieces
    return False, used_tiles

def reconstruct(pieces):
    image = [""]*size*8
    for i in range(size):
        for j in range(size):
            cropped = pieces[i*size+j].get_cropped_tile()
            for k in range(8):
                tmp = cropped[k]
                image[i*8+k] += tmp
    return image

all_pieces = []
for key, value in all_tiles.items():
    all_pieces.append(piece(key, value))

for p in all_pieces:
    for r in range(4):
        p.rotate()
        for f in range(2):
            p.flip()
            result, pieces = solve_puzzle([p])
            if result:
                for i in range(size):
                    for j in range(size):
                        print(pieces[i*size+j].nb, end=" ")
                    print()
                print(reconstruct(pieces))
                print("---- End ---")