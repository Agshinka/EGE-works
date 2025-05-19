from itertools import *
k=0
for n in product(sorted('MAНГУCT'), repeat = 6):
    s = ''.join(n)
    k+=1
    if s[0] != 'У' and s.count('M') == 2 and s.count('Г') <= 1:
        print(k)