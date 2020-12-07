c=0
for g in open('input.txt').read().split('\n\n'):
 f=g.replace('\n',' ').split()
 k=set(f[0])
 for i in f[1:]:k=k.intersection(i)
 c+=len(k)
print(c)