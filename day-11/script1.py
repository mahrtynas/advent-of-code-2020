def update_seat(m, i, j):
    count_occupied = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if (x == 0 and y == 0) or i + x < 0 or j + y < 0:
                continue
            else:
                try:
                    if m[i+x][j+y] == "#":
                        count_occupied += 1
                except IndexError:
                    continue
    if count_occupied == 0:
        return "#"
    elif count_occupied >= 4:
        return "L"
    else:
        return m[i][j]


def update_map(m):
    new_m = [[_ for _  in row] for row in m]
    for i, row in enumerate(m):
        for j, seat in enumerate(row):
            if seat in ['L', '#']:
                new_m[i][j] = update_seat(m, i, j)
    return new_m



def main():
    with open("input.txt") as f:
        rows = f.read().splitlines()
    seat_map = [[x for x in y] for y in rows]
    i = 0
    while True:
        i += 1
        print(i)
        new_seat_map = update_map(seat_map)
        a = set([tuple(x) for x in new_seat_map]) 
        b = set([tuple(x) for x in seat_map])
        if a.intersection(b) == b:
            break
        seat_map = new_seat_map
    flat = "".join(["".join(x) for x in seat_map])
    print("Occupied seats: %s" % flat.count("#"))



if __name__ == "__main__":
    main()