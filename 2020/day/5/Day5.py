def get_seat(bsp, seats=[x for x in range(128)]):
    for x in range(len(bsp)-3 if len(bsp) > 3 else len(bsp)):
        seats = seats[:int(len(seats)/2)] if bsp[x] in ['F', 'L'] else seats[int(len(seats)/2):]
    if len(bsp) == 3:
        return seats
    return seats[0], get_seat(bsp[-3:], [x for x in range(8)])[0]


with open("input.txt", "r") as file:
    data = [x.strip() for x in file.read().splitlines()]
    ids = [get_seat(bsp)[0]*8+get_seat(bsp)[1] for bsp in data]
    rc = sorted([get_seat(bsp) for bsp in data])
    seat = [(x[0],(x[1]+1)%8) for x in rc if (x[0],(x[1]+1)%8) not in rc][1:-1][0]
    print("Part 1: {}".format(max(ids)))
    print("Part 2: {}".format(seat[0]*8+seat[1]))