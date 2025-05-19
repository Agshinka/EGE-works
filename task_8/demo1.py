from itertools import *
k=0
for n in product('0123456789ab', repeat = 5):
    s = ''.join(n)
    if s.count('7') == 1 and ((s.count('9') + s.count('a') + s.count('b')) <= 3):
        if s[0] != '0':
            k+=1
print(k)