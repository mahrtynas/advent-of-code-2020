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
    counts = []
    for i in range(1, 4):
        counts.append(diffs.count(i))
        print("%s-jolt differences: %s" % (i, counts[i-1]))
    print("Result: %s x %s = %s" % (counts[0], counts[2], counts[0] * counts[2]))


if __name__ == "__main__":
    main()
