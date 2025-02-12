from itertools import *
k=0
for n in permutations ('ДЕМЬЯН'):
    s = ''.join(n)
    if s[0] != 'Ь' and 'ЕЬ' not in s and 'ЯЬ' not in s:
        k+=1
print(k)