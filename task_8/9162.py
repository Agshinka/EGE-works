from itertools import *
k=0
for n in product(sorted('МСТФ'), repeat = 4):
    s = ''.join(n)
    k+=1
    if k == 138:
        print(s, k)