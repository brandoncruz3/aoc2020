def readinput(inpath="input.txt"):
    with open(inpath, 'r') as infile:
        return list(map(int, infile.read().splitlines()))


def isValid(i, xmas):
    target = xmas[i]
    prev = xmas[i-25: i]
    if prev.count(target/2) > 1:
        return True
    prevSet = set(prev)
    prevSet.discard(target/2)
    for num in prevSet:
        if target-num in prevSet:
            return True
    return False


def p1(xmas):
    for i in range(25, len(xmas)):
        if not isValid(i, xmas):
            return xmas[i]


def p2(xmas):
    target = p1(xmas)
    for i, num in enumerate(xmas):
        run = [num]
        next = i+1
        while sum(run) < target:
            run.append(xmas[next])
            next += 1
        if len(run) >= 2 and sum(run) == target:
            return min(run) + max(run)


def main():
    xmas = readinput()
    print(f"P1: {p1(xmas)}\nP2: {p2(xmas)}")


main()