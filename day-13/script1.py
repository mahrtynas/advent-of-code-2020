def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    timestamp = int(lines[0])
    ids = [int(x) for x in lines[1].split(",") if x != "x"]
    arrivals = [x - (timestamp % x) for x in ids]
    arrives_in = min(arrivals)
    bus = ids[arrivals.index(arrives_in)]
    print("First bus to arrive: %s, wait: %s, answer: %s" % (bus, arrives_in, bus * arrives_in))


if __name__ == "__main__":
    main()