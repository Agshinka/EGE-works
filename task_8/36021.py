from itertools import *
k = 0
for n in product('ВИШНЯ', repeat = 6):
    s = ''.join(n)
    if s.count('В') <= 1 and s[0] != 'Ш' and s[-1] != 'И' and s[-1] != 'Я':
        k+=1
print(k)