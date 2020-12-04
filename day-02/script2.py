def is_password_valid(txt):
    policy, pwd = [x.strip() for x in txt.split(":")]
    pos, char = policy.split(" ")
    pos = [int(x) - 1 for x in pos.split("-")]
    if (pwd[pos[0]] == char) != (pwd[pos[1]] == char):
        return True
    else:
        return False


def main():
    with open("input.txt", "r") as f:
        entries = f.read().splitlines()
    valid_passwords = 0
    for entry in entries:
        if is_password_valid(entry):
            valid_passwords += 1
    print("%s out of %s passwords are valid" % (valid_passwords, len(entries)))


if __name__ == "__main__":
    main()
