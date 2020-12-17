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
    region = np.expand_dims(region, axis = 2)
    region = np.pad(region, (2, 2))
    return region
    return region


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    region = get_initial_region(lines)
    for i in range(6):
        new_region = np.zeros(region.shape)
        for x in range(1, region.shape[0] - 1):
            for y in range(1, region.shape[1] - 1):
                for z in range(1, region.shape[2] - 1):
                    count = 0
                    for i, j, k in product([-1, 0, 1], repeat = 3):
                        if (i, j, k) == (0, 0, 0):
                            continue
                        count += region[x + i, y + j, z + k]
                    if region[x, y, z] == 1 and count in [2, 3]:
                        new_region[x, y, z] = 1
                    elif region[x, y, z] == 0 and count == 3:
                        new_region[x, y, z] = 1
        print(np.sum(new_region))
        region = np.pad(new_region, (1, 1))



if __name__ == "__main__":
    main()
