def get_triplet_prod(values, total_sum=2020):
    for i in range(len(values) - 1):
        d = set()
        target_sum = total_sum - values[i]
        for j in range(i + 1, len(values) - 1):
            if (target_sum - values[j]) in d:
                return values[i] * values[j] * (target_sum - values[j])
            d.add(values[j])
    return None

def main():
    with open("input.txt", "r") as f:
        values = [int(x) for x in f.read().splitlines()]
    result = get_triplet_prod(values)
    print(result)


if __name__ == "__main__":
    main()



