def is_valid_target(values, target):
    for i in range(len(values) - 1):
        d = set([target - x for x in values[:i] + values[(i + 1):]])
        if values[i] in d:
            return True
    print("Target %s can not be achieved" % target)
    return False


def main():
    with open("input.txt") as f:
        numbers = [int(x) for x in f.read().splitlines()]
    preamble_size = 25
    for i in range(preamble_size, len(numbers) - 1):
        target = numbers[i]
        values = numbers[(i - preamble_size):i]
        is_valid_target(values, target)


if __name__ == "__main__":
    main()