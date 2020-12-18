import re
from functools import reduce


def evaluate_operations(chars):
    while True:
        summation = re.findall("\\d+\\s\\+\\s\\d+", chars)
        if summation:
            v = sum([int(x) for x in re.findall("\\d+", summation[0])])
            chars = re.sub(rf"(?<!\d)({re.escape(summation[0])})(?!\d)", str(v), chars)
        else:
            break
    if chars.find("*") > -1:
        factors = [int(x) for x in re.findall("\\d+", chars)]
        result = reduce(lambda a, b: a * b, factors)
        return result
    else:
        return int(chars)


def evaluate_line(line):
    # print("----")
    # print(line)
    while True:
        paren = re.findall("\\([^\\(\\)]+\\)", line)
        if paren:
            for i in paren:
                v = evaluate_operations(i[1:-1])
                line = re.sub(rf"{re.escape(i)}", str(v), line)
        else:
            break
    result = evaluate_operations(line)
    # print(result)
    return result


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    cv = 0
    for line in lines:
        cv += evaluate_line(line)
    print("Sum of all lines = %s" % cv)


if __name__ == "__main__":
    main()

