import re

DIRECTIONS = ["E", "S", "W", "N"]


def move_ship(position, instruction):
    if instruction[0] == "E":
        position.update({"x": position["x"] + int(instruction[1])})
    if instruction[0] == "S":
        position.update({"y": position["y"] - int(instruction[1])})
    if instruction[0] == "W":
        position.update({"x": position["x"] - int(instruction[1])})
    if instruction[0] == "N":
        position.update({"y": position["y"] + int(instruction[1])})

    di = DIRECTIONS.index(position["facing"])
    if instruction[0] == "R":
        now_facing =  DIRECTIONS[int(di + int(instruction[1]) / 90) % 4]
        position.update({"facing": now_facing})
    if instruction[0] == "L":
        now_facing =  DIRECTIONS[int(di - int(instruction[1]) / 90) % 4]
        position.update({"facing": now_facing})
    if instruction[0] == "F":
        move_ship(position, (position["facing"], instruction[1]))


def main():
    with open("input.txt") as f:
        rows = f.read().splitlines()
    instructions = [re.findall("(.)(\\d+)", x)[0] for x in rows]
    position = {"facing": "E", "x": 0, "y": 0}
    for instruction in instructions:
        move_ship(position, instruction)
    print("The ship is in coordinate: %s" % position)
    print("Sum: %s" % (abs(position["x"]) + abs(position["y"])))


if __name__ == "__main__":
    main()