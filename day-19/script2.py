import re
from functools import reduce
from itertools import product


def combine_rules(rules, *args):
    rr = []
    for arg in args:
        x = process_rule(rules, arg)
        rr.append(x)
    result = ["".join(i) for i in product(*rr)]
    return set(result)


def process_rule(rules, key):
    # each line will become a set after processing, so if it's a string
    # it has to be processed
    times = rules[key]["times"]
    rule = rules[key]["rule"]
    if type(rule) == str:
        rules[key]["times"] += 1
        if rule in ["a", "b"]:
            rules[key]["rule"] = set(rule)
        elif not re.search("\\|", rule):
            values = re.findall("(\\d+)", rule)
            result = combine_rules(rules, *[int(x) for x in values])
            rules[key]["rule"] = result
        else:
            alternatives = [x.strip() for x in rule.split("|")]
            d = []
            for alt in alternatives:
                v = re.findall("(\\d+)", alt)
                d.append(combine_rules(rules, *[int(x) for x in v]))
            result = reduce(lambda a, b: a.union(b), d)
            rules[key]["rule"] = result
        return rules[key]["rule"]
    if type(rule) == set:
        return rules[key]["rule"]

def is_message_valid(msg, r1, r2):
    l = len(list(r1)[0])
    assert l == len(list(r2)[0])
    chains = [msg[i:i+l] for i in range(0, len(msg), l)]
    result = []
    for chain in chains:
        if chain in r1:
            result.append(1)
        elif chain in r2:
            result.append(2)
        else:
            return False
    if result[-1] == 1:
        return False
    if result.count(2) >= result.count(1):
        return False
    result_sorted = [x for x in result]
    result_sorted.sort()
    if result != result_sorted:
        return False
    print(result)
    return True


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    rules = {}
    i = 0
    while lines[i] != "":
        rule = {int(x): {"rule": y.strip('"'), "times": 0} for x, y in re.findall('(\\d+).{2}(.+)', lines[i])}
        rules |= rule
        i += 1
    valid_values = process_rule(rules, 0)

    # 8: 42 | 42 8
    # 8: 42 | 42 (42 | 42 8) = 42 | 42 42 | 42 42 8

    # 11: 42 31 | 42 11 31
    # 11: 42 31 | 42 (42 31 | 42 11 31) 31
    # 11: 42 31 | 42 42 31 31 | 42 42 11 31 31
     
    count_valid = 0
    for j in range(i + 1, len(lines)):
        count_valid += is_message_valid(lines[j], rules[42]["rule"], rules[31]["rule"])
    print("Number of valid messages: %s out of %s" % (count_valid, len(lines) - i))


if __name__ == "__main__":
    main()

