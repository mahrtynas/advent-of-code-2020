import re


def parse_documents(lines):
    documents = [x.replace("\n", " ") for x in lines.split("\n\n")]
    return [set(re.findall("[a-z]+(?=\:)", x)) for x in documents]


def main():
    with open("input.txt", "r") as f:
        lines = f.read()
    docs = parse_documents(lines)
    required = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    valid = 0
    for doc in docs:
        if doc.intersection(required) == required:
            valid += 1
    print(valid)


if __name__ == "__main__":
    main()