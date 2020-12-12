import re
import math


def update_waypoint(waypoint, instruction):
    if instruction[0] == "E":
        waypoint.update({"dx": waypoint["dx"] + int(instruction[1])})
    if instruction[0] == "S":
        waypoint.update({"dy": waypoint["dy"] - int(instruction[1])})
    if instruction[0] == "W":
        waypoint.update({"dx": waypoint["dx"] - int(instruction[1])})
    if instruction[0] == "N":
        waypoint.update({"dy": waypoint["dy"] + int(instruction[1])})
    if instruction[0] in ["R", "L"]:
        a = int(instruction[1]) * (-1 if instruction[0] == "R" else 1)
        a = math.radians(a)
        dx = waypoint["dx"]
        dy = waypoint["dy"]
        waypoint.update({
            "dx": round(math.cos(a) * dx - math.sin(a) * dy),
            "dy": round(math.sin(a) * dx + math.cos(a) * dy)}
            )


def move_ship(position, waypoint, times):
    position.update({
        "x": position["x"] + waypoint["dx"] * times,
        "y": position["y"] + waypoint["dy"] * times
        })


def main():
    with open("input.txt") as f:
        rows = f.read().splitlines()
    instructions = [re.findall("(.)(\\d+)", x)[0] for x in rows]
    position = {"x": 0, "y": 0}
    waypoint = {"dx": 10, "dy": 1}
    for instruction in instructions:
        if instruction[0] == "F":
            move_ship(position, waypoint, int(instruction[1]))
        else:
            update_waypoint(waypoint, instruction)
    print("The ship is in coordinate: %s" % position)
    print("Sum: %s" % (abs(position["x"]) + abs(position["y"])))


if __name__ == "__main__":
    main()