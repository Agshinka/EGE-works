from itertools import *
k=0
for n in permutations('ЛЕВИЙ'):
    s = ''.join(n)
    if s[0] != 'Й' and 'ЕИ' not in s:
        k+=1
print(k)