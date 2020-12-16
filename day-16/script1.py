import re
from functools import reduce


def process_parameters(line):
    key = re.match(".*(?=\\:)", line)[0]
    values = [int(x) for x in re.findall("\\d+", line)]
    set_1 = set([x for x in range(values[0], values[1] + 1)])
    set_2 = set([x for x in range(values[2], values[3] + 1)])
    return {key: set_1.union(set_2)}



def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    i = 0
    parameters = {}
    while lines[i]:
        d = process_parameters(lines[i])
        parameters |= d
        i += 1
    all_params = reduce(lambda a, b: a.union(b), parameters.values())
    i += 2
    my_ticket = [int(x) for x in lines[i].split(",")]
    i += 3
    other_tickets = []
    for j in range(i, len(lines)):
        other_tickets += [int(x) for x in lines[j].split(",")]
    cv = 0
    for v in other_tickets:
        if v not in all_params:
            cv += v
    print(cv)



if __name__ == "__main__":
    main()