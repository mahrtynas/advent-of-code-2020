import math

def is_tree(p, pattern, n):
    trees = set(i for i, x in enumerate(pattern) if x == "#")
    if p % n in trees:
        return True
    return False

def main():
    with open("input.txt", "r") as f:
        forest = f.read().splitlines()
    N = len(forest)
    n = len(forest[0])
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    slope_trees = []
    for slope in slopes:
        pos = [[slope[0] * i, x] for i, x in enumerate(range(0, N, slope[1]))]
        trees = 0
        for p in pos:
            if is_tree(p[0], forest[p[1]], n):
                trees += 1
        print("Number of trees: %s" % trees)
        slope_trees.append(trees)
    print("List of trees: %s" % slope_trees)
    print("Multiplied: %s" % math.prod(slope_trees))


if __name__ == "__main__":
    main()


