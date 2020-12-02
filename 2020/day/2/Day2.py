import re
import itertools

print(len([pwd for [f,t,c,pwd] in (re.match(r'^([0-9]+)-([0-9]+) ([a-z]): (\w+)', l).groups() for l in open('input.txt')) if {k:len(list(g)) for k,g in itertools.groupby(sorted(pwd))}.get(c) in range(int(f),int(t)+1)]))
print(len([pwd for [f,t,c,pwd] in (re.match(r'^([0-9]+)-([0-9]+) ([a-z]): (\w+)', l).groups() for l in open('input.txt')) if (pwd[int(f)-1]==c)^(pwd[int(t)-1]==c)]))