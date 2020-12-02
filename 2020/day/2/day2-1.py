data = open('input.txt', 'r').read().split('\n')

# Part 1
invalid_passwords = 0
valid_passwords = 0

for i in data:
    key, password = i.split(": ")
    min = int(key.split("-")[0])
    max = int(key.split("-")[1].split(" ")[0])
    letter = key.split("-")[1].split(" ")[1]
    count = password.count(letter)
    if count < min or count > max:
        invalid_passwords += 1
    if count >= min and count <= max:
        valid_passwords += 1

print(f"Part 1. Valid: {valid_passwords}, Invalid: {invalid_passwords}")

# Part 2
invalid_passwords = 0
valid_passwords = 0

for i in data:
    key, password = i.split(": ")
    pos1 = int(key.split("-")[0])
    pos2 = int(key.split("-")[1].split(" ")[0])
    letter = key.split("-")[1].split(" ")[1]
    if (password[pos1-1] == letter and password[pos2-1] != letter) or \
            (password[pos1-1] != letter and password[pos2-1] == letter):
        valid_passwords += 1
    else:
        invalid_passwords += 1

print(f"Part 2. Valid: {valid_passwords}, Invalid: {invalid_passwords}")