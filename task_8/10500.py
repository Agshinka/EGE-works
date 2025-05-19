from itertools import *
k=0
for n in product('12345', repeat = 5):
    s = ''.join(n)
    if s.count('1') == 3:
        k+=1
print(k)