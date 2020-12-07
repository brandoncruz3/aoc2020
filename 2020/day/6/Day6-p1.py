c=0
for p in open('input.txt').read().split('\n\n'):c+=len(set(p.replace('\n','')))
print(c)

