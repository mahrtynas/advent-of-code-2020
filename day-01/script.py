def search(values, sum_value=2020):
    for i, x in enumerate(values):
        if x + values[i+1] <= sum_value:
            for j, y in enumerate(values[i+1:]):
                if x + y == sum_value:
                    return "%s + %s = %s and %s * %s = %s" % (
                        x, y, x + y, x, y, x * y

                        )


def main():
    with open("input.txt", "r") as f:
    	input = [int(x) for x in f.read().splitlines()]
    input.sort()
    result = search(input)
    print(result)


if __name__ == "__main__":
    main()
