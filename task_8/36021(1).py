from itertools import *
k=0
for n in product('ВИШНЯ', repeat = 6):
    s = ''.join(n)
    if s[0] != 'Ш' and s[-1] != 'И' and s[-1] != 'Я':
        if s.count('В') <= 1:
            k+=1
print(k)