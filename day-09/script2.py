def is_valid_target(values, target):
    for i in range(len(values) - 1):
        d = set([target - x for x in values[:i] + values[(i + 1):]])
        if values[i] in d:
            return True
    print("Target %s can not be achieved" % target)
    return False


def find_contiguous_set(values, target):
    while True:
        v = values.pop(-1)
        t = v
        i = 0
        while t <= target:
            t += values[(-1-i)]
            if t == target:
                d = set(values[(-1-i):] + [v])
                print("Set %s sums to %s" % (d, target))
                print("Max: %s, min: %s, sum = %s" % (max(d), min(d), max(d) + min(d)))
                return
            i += 1


def main():
    with open("input.txt") as f:
        numbers = [int(x) for x in f.read().splitlines()]
    preamble_size = 25
    for i in range(preamble_size, len(numbers) - 1):
        target = numbers[i]
        values = numbers[(i - preamble_size):i]
        if not is_valid_target(values, target):
            find_contiguous_set(numbers[:i], target)


if __name__ == "__main__":
    main()