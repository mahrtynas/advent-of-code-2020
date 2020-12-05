def decode_seat_id(boarding_pass):
    row = int("".join(["0" if x == 'F' else "1" for x in boarding_pass[0:7]]), 2)
    seat = int("".join(["0" if x == 'L' else "1" for x in boarding_pass[7:10]]), 2)
    return row * 8 + seat


def main():
    with open("input.txt", "r") as f:
        boarding_passes = f.read().splitlines()
    max_id = 0
    for boarding_pass in boarding_passes:
        seat_id = decode_seat_id(boarding_pass)
        if seat_id > max_id:
            max_id = seat_id
    print("Highest seat id: %s" % max_id)


if __name__ == "__main__":
    main() 
