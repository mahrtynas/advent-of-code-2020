def my_sum(n):
    ls = [0, 1]
    for i in range(n):
        ls.append(sum(ls[-3:]))
    print(ls)
    return sum(ls[-3:])

def main():
    with open("input.txt", "r") as f:
        adapters = [int(x) for x in f.read().splitlines()]
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    diffs = []
    for i, adapter in enumerate(adapters):
        if i == 0:
            diffs.append(adapter)
        else:
            diffs.append(adapter - adapters[i-1])
    print(diffs)
    ways = 1
    i = 0
    combo_of_ones = 0
    while i < len(diffs):
        if diffs[i] == 1:
            combo_of_ones += 1
        else:
            ways *= my_sum(combo_of_ones-1)
            combo_of_ones = 0
        i += 1
    print("Possible ways: %s" % ways)


if __name__ == "__main__":
    main()
