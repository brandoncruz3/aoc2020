with open("input.txt", "r") as file:
    jolts = sorted([int(x.strip()) for x in file.read().splitlines()])
    jolts = [0] + jolts + [max(jolts)+3]
    print(jolts)
    print(len([jolts[x] for x in range(1, len(jolts)) if jolts[x]-jolts[x-1] == 1]))
    print(len([jolts[x] for x in range(1, len(jolts)) if jolts[x]-jolts[x-1] == 3]))
    print('P1: {}'.format(len([jolts[x] for x in range(1, len(jolts)) if jolts[x]-jolts[x-1] == 1])*len([jolts[x] for x in range(1, len(jolts)) if jolts[x]-jolts[x-1] == 3])))
    
    arrangements = {jolts[0]:1}
    for x in jolts[1:]:
        arrangements[x] = sum(arrangements[x-y] for y in range(1,4) if x-y in arrangements)
    print(arrangements[jolts[-1]])
    print('P2: {}'.format(arrangements[jolts[-1]]))