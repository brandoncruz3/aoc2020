import re

def get_data():
  with open("input.txt") as f:
    return [x for x in f.read().split("\n\n") if x]

def p1():
  p1 = 0
  fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
  for line in get_data():
    p1 += all(x in line for x in fields)
  return p1

def p2():
    p2 = 0
    fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
    for line in get_data():
        if all(x in line for x in fields):
            byr = re.search('byr:([^ \n]+)', line).groups()[0]
            iyr = re.search('iyr:([^ \n]+)', line).groups()[0]
            eyr = re.search('eyr:([^ \n]+)', line).groups()[0]
            hgt = re.search('hgt:([^ \n]+)', line).groups()[0]
            hcl = re.search('hcl:([^ \n]+)', line).groups()[0]
            ecl = re.search('ecl:([^ \n]+)', line).groups()[0]
            pid = re.search('pid:([^ \n]+)', line).groups()[0]
            
            p2 += \
                re.match('^[0-9]{4}', byr) != None and 1920 <=int(byr) <= 2002 and \
                re.match('^[0-9]{4}$', iyr) != None and 2010 <= int(iyr) <= 2020 and \
                re.match('^[0-9]{4}$', eyr) != None and 2020 <= int(eyr) <= 2030 and \
                re.match('^((1([5-8][0-9]|9[0-3]))cm|(59|6[0-9]|7[0-6])in)$', hgt) != None and \
                re.match('^#[0-9a-z]{6}$', hcl) != None and \
                re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', ecl) != None and \
                re.match('^[0-9]{9}$', pid) != None
    return p2
    
def main():
  print(f'P1: {p1()}')
  print(f'P2: {p2()}')
  return 0

if __name__ == '__main__':
  main()