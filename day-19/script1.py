import re
from functools import reduce
from itertools import product


def combine_rules(rules, *args):
    rr = []
    for arg in args:
        rr.append(process_rule(rules, arg))
    # now both rules are definitely sets
    result = []
    for i in product(*rr):
        result.append("".join(i))
    return set(result)


def process_rule(rules, key):
    # each line will become a set after processing, so if it's a string
    # it has to be processed
    if type(rules[key]) == str:
        if rules[key] in ["a", "b"]:
            rules[key] = set(rules[key])
        elif not re.search("\\|", rules[key]):
            values = re.findall("(\\d+)", rules[key])
            result = combine_rules(rules, *[int(x) for x in values])
            rules[key] = result
        else:
            alternatives = [x.strip() for x in rules[key].split("|")]
            d = []
            for alt in alternatives:
                v = re.findall("(\\d+)", alt)
                d.append(combine_rules(rules, *[int(x) for x in v]))
            result = reduce(lambda a, b: a.union(b), d)
            rules[key] = result
        return rules[key]
    if type(rules[key]) == set:
        return rules[key]


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    rules = {}
    i = 0
    while lines[i] != "":
        rule = {int(x): y.strip('"') for x, y in re.findall('(\\d+).{2}(.+)', lines[i])}
        rules |= rule
        i += 1
    # process rules starting with 0
    valid_values = process_rule(rules, 0)
    count_valid = 0
    for j in range(i + 1, len(lines)):
        count_valid += lines[j] in rules[0]
    print("Number of valid messages: %s" % count_valid)


if __name__ == "__main__":
    main()

