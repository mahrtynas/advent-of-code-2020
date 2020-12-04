def is_password_valid(txt):
    policy, pwd = txt.split(":")
    times, char = policy.split(" ")
    min_t, max_t = [int(x) for x in times.split("-")]
    if pwd.count(char) >= min_t and pwd.count(char) <= max_t:
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
