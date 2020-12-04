import re

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
    pos = [3 * x for x in range(N)]
    trees = 0
    for i, road in enumerate(forest):
        if is_tree(pos[i], road, n):
            trees += 1
    print("Number of trees: %s" % trees)


if __name__ == "__main__":
    main()


