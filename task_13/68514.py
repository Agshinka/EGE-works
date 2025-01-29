print('0' + bin(122)[2:], bin(159)[2:], bin(136)[2:] , bin(144)[2:])

print(bin(255)[2:], bin(255)[2:], bin(255)[2:], bin(248)[2:])

from itertools import *
k = 0
for n in product ([0,1], repeat = 3):
    if (14 + sum(n)) % 4 != 0:
        k+=1
print(k)