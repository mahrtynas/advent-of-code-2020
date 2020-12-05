def decode_seat_id(boarding_pass):
    row = int("".join(["0" if x == 'F' else "1" for x in boarding_pass[0:7]]), 2)
    seat = int("".join(["0" if x == 'L' else "1" for x in boarding_pass[7:10]]), 2)
    return row * 8 + seat


def main():
    with open("input.txt", "r") as f:
        boarding_passes = f.read().splitlines()
    seat_ids = [decode_seat_id(x) for x in boarding_passes]
    min_id, max_id = (min(seat_ids), max(seat_ids))
    all_ids = set([_ for _ in range(min_id, max_id)])
    missing = all_ids.difference(seat_ids)
    print("Missing ids: %s" % missing)


if __name__ == "__main__":
    main() 
