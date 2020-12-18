import re


def evaluate_operations(chars):
    ops = chars.split(" ")
    v = int(ops[0])
    for i in range(2, len(ops), 2):
        if ops[i - 1] == "*":
            v *= int(ops[i])
        elif ops[i - 1] == "+":
            v += int(ops[i])
    return v


def evaluate_line(line):
    # check 
    while True:
        paren = re.findall("\\([^\\(\\)]+\\)", line)
        if paren:
            for i in paren:
                v = evaluate_operations(i[1:-1])
                line = re.sub(rf"{re.escape(i)}", str(v), line)
        else:
            break
    result = evaluate_operations(line)
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

