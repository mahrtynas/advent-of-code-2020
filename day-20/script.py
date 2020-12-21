import numpy as np
import re


# process sea monster
SEA_MONSTER_STR = [
"                  # ",
"#    ##    ##    ###",
" #  #  #  #  #  #   ",
]

class Tile:
    def __init__(self, image_data, tile_id):
        self.id = tile_id
        self.image = image_data
        self.side_arrays = {
            "up": image_data[0, :],
            "right": image_data[:, -1],
            "down": image_data[-1, :],
            "left": image_data[:, 0],
        }
        
        self.cards = {
            "up": None,
            "right": None,
            "down": None,
            "left": None
        }
        self.flipped = [False, False] # h and v
        self.rotated = 0
        self.matched = False
        self.trimmed_image = None

    def __str__(self):
        print("Tile %s" % self.id)
        for x in self.image:
            print(x)
        return ""

    def update_side_arrays(self):
        self.side_arrays = {
            "up": self.image[0, :],
            "right": self.image[:, -1],
            "down": self.image[-1, :],
            "left": self.image[:, 0],
        }


    def flip(self, direction="h"):
        check = sum([1 if x is not None else 0 for x in self.cards.values()])
        if check > 0:
            return
        if direction == "h":
            self.image = self.image[:,::-1]
            self.flipped[0] = not self.flipped[0]
            self.update_side_arrays()
        if direction == "v":
            self.image = self.image[::-1,:]
            self.flipped[1] = not self.flipped[1]
            self.update_side_arrays()

    def rotate(self, angle=90):
        check = sum([1 if x is not None else 0 for x in self.cards.values()])
        if check > 0:
            return
        self.image = self.image.transpose()[:,::-1]
        self.update_side_arrays()
        self.rotated = (self.rotated + 90) % 360


    def match_tile(self, tile, side):
        sides = ["up", "right", "down", "left"]
        op_side = sides[(sides.index(side) + 2) % 4]
        i = 0
        matched = False
        while i < 8 and not matched:
            if np.all(self.side_arrays[side] == tile.side_arrays[op_side]):
                matched = True
                self.cards[side] = tile
                tile.cards[op_side] = self
                tile.matched = True
                return True 
            tile.rotate()
            if i == 3:
                d = "h" if side in ["up", "down"] else "v"
                tile.flip(d)
            i += 1
        if not matched:
            return False

    def trim_borders(self):
        self.trimmed_image = self.image[1:-1,1:-1]
        return self.trimmed_image

    def get_row_image(self):
        row = self.trim_borders()
        tile = self
        while tile.cards["right"] is not None:
            row = np.hstack((row, tile.cards["right"].trim_borders()))
            tile = tile.cards["right"]
        return row



def read_tiles(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    tiles = []
    i = 0
    l = []
    while i < len(lines):
        if re.match("Tile", lines[i]):
            tile_id = int(re.findall("\\d+", lines[i])[0])
            i += 1
            continue
        if re.match("[\\.\\#]", lines[i]):
            l.append([1 if x == "#" else 0 for x in lines[i]])
            i += 1
            continue
        tiles.append(Tile(np.array(l), tile_id))
        l = []
        i += 1
    tiles.append(Tile(np.array(l), tile_id))
    return tiles


def convert_sea_monster(inp = SEA_MONSTER_STR):
    sea_monster = []
    for line in inp:
        sea_monster.append([1 if x == "#" else 0 for x in line])
    sea_monster = np.array(sea_monster)
    return sea_monster

def find_sea_monsters(image, monster):
    h, w = monster.shape
    ih, iw = image.shape
    count = 0
    for i in range(ih - h):
        for j in range(iw - w):
            sub_image = image[i:(i+h), j:(j+w)]
            sub_image = np.where(monster, sub_image, 0)
            if np.all(sub_image == monster):
                count += 1
    return count

def main():
    tiles = read_tiles("input.txt")
    sides = ["up", "right", "down", "left"]
    tiles[0].matched = True
    while True:
        stable = [x for x in tiles if x.matched]
        unstable = [x for x in tiles if not x.matched]
        if len(unstable) == 0:
            break
        for i in unstable:
            for j in stable:
                for side in sides:
                    if j.cards[side] is None:
                        match = j.match_tile(i, side)
                        if match:
                            break

    result = 1
    for tile in tiles:
        if len([x for x in tile.cards.values() if x is not None]) == 2:
            print(tile.id)
            result *= tile.id
    print("Multiplied corners: %s" % result)

    # dictionary of tiles:
    d_tiles = {tile.id: tile for tile in tiles}

    # find top left tile:
    curr_tile = None
    i = 0
    while not curr_tile:
        if (tiles[i].cards["up"] is None and tiles[i].cards["left"] is None and
            tiles[i].cards["right"] is not None and tiles[i].cards["down"] is not None):
            curr_tile = tiles[i]
        i += 1
    print("Top left tile is: %s" % curr_tile.id)

    # create image:
    full_image = curr_tile.get_row_image()
    print("one tile down: %s" % curr_tile.cards["down"].id)
    while curr_tile.cards["down"] is not None:
        print("Current tile: %s" % curr_tile.id)
        full_image = np.vstack((full_image, curr_tile.cards["down"].get_row_image()))
        curr_tile = curr_tile.cards["down"]

    # second part with sea monsters
    sea_monster = convert_sea_monster()

    # find sea monsters:
    count = 0
    i = 0
    while i < 8 and count == 0:
        count = find_sea_monsters(full_image, sea_monster)
        if count > 0:
            break
        # rotate
        full_image = full_image.transpose()[:,::-1]
        if i == 3:
            # flip
            full_image = full_image[:,::-1]
        i += 1

    # roughness
    image_hashes = np.sum(full_image)
    monster_hashes = np.sum(sea_monster)
    roughness = image_hashes - count * monster_hashes
    print("Roughness = %s" % roughness)
    

if __name__ == "__main__":
    main()
