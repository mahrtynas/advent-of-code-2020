def main():
    with open("input.txt", "r") as f:
        inp = f.read()
    groups = [x.split("\n") for x in inp.split("\n\n")]
    count = 0
    for group in groups:
        d = set()
        for pa in group:
            d = d.union(set(pa))
        print(d)
        count += len(d)
    print(count)


if __name__ == "__main__":
    main()
