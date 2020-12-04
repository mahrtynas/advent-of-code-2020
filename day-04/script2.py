import re


def parse_documents(lines):
    documents = [x.replace("\n", " ") for x in lines.split("\n\n")]
    return [dict(re.findall("([a-z]+):([^\\s]+)", x)) for x in documents]


def is_height_valid(value):
    if re.match("\\d+cm", value):
        h = int(re.match("\\d+", value)[0])
        if h >= 150 and h <= 193:
            return True
    if re.match("\\d+in", value):
        h = int(re.match("\\d+", value)[0])
        if h >= 59 and h <= 76:
            return True
    return False

def is_valid(doc):
    try:
        if int(doc["byr"]) < 1920 or int(doc["byr"]) > 2002:
            return False
        if int(doc["iyr"]) < 2010 or int(doc["iyr"]) > 2020:
            return False
        if int(doc["eyr"]) < 2020 or int(doc["eyr"]) > 2030:
            return False
        if not is_height_valid(doc["hgt"]):
            return False
        if not re.match("^#[0-9a-f]{6}$", doc["hcl"]):
            return False
        if not doc["ecl"] in set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
            return False
        if not re.match("^[0-9]{9}$", doc["pid"]):
            return False
    except KeyError:
        return False
    return True

def main():
    with open("input.txt", "r") as f:
        lines = f.read()
    docs = parse_documents(lines)
    valid = 0
    for doc in docs:
        if is_valid(doc):
            valid += 1
    print(valid)


if __name__ == "__main__":
    main()