from itertools import *
k=0
for n in product(sorted('АОУ'), repeat = 5):
    s = ''.join(n)
    k+=1
    if s == 'УАУАУ':
        print(k)