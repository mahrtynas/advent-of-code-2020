import numpy as np
from itertools import product


def get_initial_region(lines):
    region = None
    for line in lines:
        arr = np.array([1 if x == "#" else 0 for x in line])
        if region is None:
            region = arr
        else:
            region = np.vstack((region, arr))
    region = np.expand_dims(region, axis = (2, 3))
    region = np.pad(region, (2, 2))
    return region


def main():
    with open("test_input.txt") as f:
        lines = f.read().splitlines()
    region = get_initial_region(lines)
    for i in range(6):
        new_region = np.zeros(region.shape)
        x_r = range(1, region.shape[0] - 1)
        y_r = range(1, region.shape[1] - 1)
        z_r = range(1, region.shape[2] - 1)
        w_r = range(1, region.shape[3] - 1)
        for x, y, z, w in product(x_r, y_r, z_r, w_r):
            count = 0
            for i, j, k, l in product([-1, 0, 1], repeat = 4):
                if (i, j, k, l) == (0, 0, 0, 0):
                    continue
                count += region[x + i, y + j, z + k, w + l]
            if region[x, y, z, w] == 1 and count in [2, 3]:
                new_region[x, y, z, w] = 1
            elif region[x, y, z, w] == 0 and count == 3:
                new_region[x, y, z, w] = 1
        print(np.sum(new_region))
        region = np.pad(new_region, (1, 1))



if __name__ == "__main__":
    main()
