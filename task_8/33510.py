from itertools import *
k=0
for n in product ('ТИМОФЕЙ', repeat = 5):
    s = ''.join(n)
    if s.count('Т') >= 1:
        if s.count('Й') <= 1:
            k+=1
print(k)