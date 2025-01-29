print('0' + bin(112)[2:], bin(160)[2:], '0' * 8 , '0' * 8)

print(bin(255)[2:], bin(240)[2:], '0' * 8, '0' * 8)

from itertools import *
k = 0
for n in product ([0,1], repeat = 20):
    if (5 + sum(n)) % 5 != 0:
        k+=1
print(k)