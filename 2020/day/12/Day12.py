from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=12)

example = """F10
N3
F7
R90
F11"""

# commands = [(line[0], int(line[1:])) for line in example.split("\n")]
commands = [(line[0], int(line[1:])) for line in puzzle.input_data.split("\n")]

facings = {
    "F": "E",
    "R": ["N", "E", "S", "W"],
    "L": ["N", "W", "S", "E"],
    "N": complex(0 + 1j),
    "E": complex(1 + 0j),
    "S": complex(0 - 1j),
    "W": complex(-1 + 0j)
}


def get_complex_distance(complex1, complex2):
    return int(abs(complex1.real - complex2.real) + abs(complex1.imag - complex2.imag))


def turn(direction, degrees):
    quarter_turns = int(degrees / 90)
    current_facing = facings["F"]
    facing_position = facings[direction].index(current_facing)
    new_position = int((facing_position + quarter_turns) % 4)
    new_direction = facings[direction][new_position]
    facings["F"] = new_direction


def turn_waypoint(direction, degrees, waypoint):
    quarter_turns = int(degrees / 90)

    for flip in range(quarter_turns):
        if direction == "L":
            # (x, y) = (-y, x)
            waypoint = complex(-waypoint.imag, waypoint.real)
        else:
            # (x, y) = (y, -x)
            waypoint = complex(waypoint.imag, -waypoint.real)

    return waypoint


def move(direction, amount):
    if direction == "F":
        direction = facings["F"]

    return facings[direction] * amount


# Part 1
original_point = complex(0 + 0j)
current_point = complex(0 + 0j)
for command in commands:
    if command[0] in ("L", "R"):
        turn(command[0], command[1])
    else:
        current_point += move(command[0], command[1])

print(get_complex_distance(original_point, current_point))

# Part 2
original_point = complex(0 + 0j)
current_point = complex(0 + 0j)
waypoint = complex(10 + 1j)
for command in commands:
    if command[0] in ("L", "R"):
        waypoint = turn_waypoint(command[0], command[1], waypoint)
    elif command[0] in ("N", "S", "E", "W"):
        waypoint += move(command[0], command[1])
    elif command[0] in "F":
        current_point += waypoint * command[1]

print(get_complex_distance(original_point, current_point))