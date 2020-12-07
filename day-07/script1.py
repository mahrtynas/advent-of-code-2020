import re


def parse_description(s, target="shiny gold"):
    color = re.match(".*(?=\\sbags\\scontain)", s)[0]
    contain = re.findall("(\\d)\\s([^\\,]+)(?=\\sbag)", s)
    contain_colors = [x[1] for x in contain]
    d = {
        color : {
            "contain": contain_colors,
            "has_target": None
        }
        
    }
    if not contain_colors:
        d[color]["has_target"] = False
    elif target in contain_colors:
        d[color]["has_target"] = True
    return d


def can_have_target(bags, color, target="shiny gold"):
    if color == target:
        return False
    if bags[color]["has_target"] is not None:
        return bags[color]["has_target"]
    else:
        res = []
        for subcolor in bags[color]["contain"]:
            res.append(can_have_target(bags, subcolor))
    bags[color]["has_target"] = sum(res) > 0
    return bags[color]["has_target"]


def main():
    with open("input.txt", "r") as f:
        descriptions = f.read().splitlines()
    bags = {}
    for d in descriptions:
        bags |= parse_description(d)
    count = 0
    for key in bags.keys():
        if can_have_target(bags, key):
            count += 1
            print(key)
    print(count)
    


if __name__ == "__main__":
    main()
