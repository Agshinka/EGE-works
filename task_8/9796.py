from itertools import *
k=0
for n in product('АВСХ', repeat = 5):
    s = ''.join(n)
    if s.count('Х') == 1:
        k+=1
print(k)