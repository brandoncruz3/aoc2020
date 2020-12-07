from collections import defaultdict, deque

colors1 = defaultdict(list)
colors2 = defaultdict(list)

def get_input():
    with open('input.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]

def main():
    file = get_input()
    for line in file:
        parent, tokens = [s for s in line.split(' bags contain ')]
        for token in tokens.replace('.', '').split(', '):
            if token != 'no other bags':
                num = int(token[0])
                child = token[2:].split(' bag')[0].strip()
                colors1[child].append((num, parent)) # Contains parent colors for each color
                colors2[parent].append((num, child)) # Contains child colors for each color
    print('Part 1:', part1('shiny gold'))
    print('Part 2:', part2('shiny gold'))

def part1(root):
    final = []
    temp = deque([root])
    while len(temp) > 0:
        for ID in filter(lambda m: m == temp[-1], colors1.keys()):
            for color in filter(lambda n: n[1] not in final and n[1] not in temp, colors1[ID]):
                temp.appendleft(color[1])
        final.append(temp.pop())
    return len(final) - 1

def part2(root):
    total = 0
    for num, color in colors2[root]:
        total += num + (num * part2(color))
    return total

if __name__ == "__main__":
    main()