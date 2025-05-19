from itertools import *
k=0
b=[]
for n in product(sorted('КОМПЬТЕР'), repeat = 5):
    s = ''.join(n)
    k+=1
    if s.count('К') == 0 and s.count('Р') == 2:
        b.append(k)
print(b[-1])