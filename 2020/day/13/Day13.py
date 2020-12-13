import time
import math
from aocd import lines

start=time.time()
timestamp=int(lines[0])
busses=[int(x) if x!='x' else 0 for x in lines[1].split(',')]
dep=[]
bestbus=0
for b in busses:
    if b!=0:
        dep+=[math.ceil(timestamp/b)*b]
        bestbus=b if math.ceil(timestamp/b)*b==min(dep) else bestbus
print('p1',(min(dep)-timestamp)*bestbus)

i=0
M=1
e=0
#with ChineseRemainderTheorem
for x in busses:
    if x!=0: M*=x
j=0
while j<len(busses):
    while busses[j]==0: j+=1
    e+=-j*(M//busses[j])*pow(M//busses[j],-1,busses[j])
    j+=1
print('p2',e%M)
end=time.time()
print(round(end-start,6))