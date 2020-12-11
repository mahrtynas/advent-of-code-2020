def update_seat(m, i, j):
    count_occupied = 0
    directions = [
        [-1, 0], # north 
        [-1, 1], # north east
        [0, 1],  # east
        [1, 1], # south east
        [1, 0], # south
        [1, -1], # south west
        [0, -1], # west
        [-1, -1] # north west        
        ]
    for d in directions:
        v = d[0]
        h = d[1]
        found = False
        while i + v in range(len(m)) and j + h in range(len(m[0])) and m[i + v][j + h] != "L" and not found:
            if m[i + v][j + h] == "#":
                count_occupied += 1
                found = True
            v += d[0]
            h += d[1]
    if count_occupied == 0:
        return "#"
    elif count_occupied >= 5:
        return "L"
    else:
        return m[i][j]


def update_map(m):
    new_m = [[_ for _  in row] for row in m]
    for i, row in enumerate(m):
        for j, seat in enumerate(row):
            if seat in ['L', '#']:
                new_m[i][j] = update_seat(m, i, j)
    # for row in new_m:
    #     print("".join(row))
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
