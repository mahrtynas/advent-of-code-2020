import re
from functools import reduce


def process_parameters(line):
    key = re.match(".*(?=\\:)", line)[0]
    values = [int(x) for x in re.findall("\\d+", line)]
    set_1 = set([x for x in range(values[0], values[1] + 1)])
    set_2 = set([x for x in range(values[2], values[3] + 1)])
    return {key: set_1.union(set_2)}

def is_valid(ticket, params):
    t = set(ticket)
    if t.intersection(params) == t:
        return True
    else:
        return False

def assign_fields(tickets, params):
    n_fields = len(tickets[0])
    matches = {x: set() for x in range(n_fields)}
    for i in range(n_fields):
        for key in params.keys():
            col_i_values = set([x[i] for x in tickets])
            if col_i_values.intersection(params[key]) == col_i_values:
                matches[i].add(key)
    l = reduce(lambda a, b: a + b, [len(x) for x in matches.values()])
    while l > len(matches.keys()):
        for key, values in matches.items():
            if len(values) == 1:
                for key_2 in matches.keys():
                    if key != key_2:
                        try:
                            matches[key_2].remove(list(matches[key])[0])
                        except KeyError:
                            continue
        l = reduce(lambda a, b: a + b, [len(x) for x in matches.values()])
    result = {x: list(y)[0] for x, y in matches.items()}
    return result



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
    all_tickets = []
    all_tickets.append(my_ticket)
    for j in range(i, len(lines)):
        ticket = [int(x) for x in lines[j].split(",")]
        if is_valid(ticket, all_params):
            all_tickets.append(ticket)
    fields = assign_fields(all_tickets, parameters)
    result = 1
    for i, v in enumerate(my_ticket):
        if re.match("departure", fields[i]):
            result *= v
    print(result)

if __name__ == "__main__":
    main()