import re


def parse_description(s):
    color = re.match(".*(?=\\sbags\\scontain)", s)[0]
    contain = re.findall("(\\d)\\s([^\\,]+)(?=\\sbag)", s)
    contain_colors = [x[1] for x in contain]
    d = {
        color : {
            "contain": contain,
        }        
    }
    return d

def count_internal_bags(bags, color):
    if not bags[color]["contain"]:
        return 0
    else:
        counter = 0
        for item in bags[color]["contain"]:
            counter += int(item[0]) * (1 + count_internal_bags(bags, item[1]))
    return counter



def main():
    with open("input.txt", "r") as f:
        descriptions = f.read().splitlines()
    bags = {}
    for d in descriptions:
        bags |= parse_description(d)
    col = "shiny gold"
    print("%s bag contains %s bags" % (col, count_internal_bags(bags, col)))
    


if __name__ == "__main__":
    main()
