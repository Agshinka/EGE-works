from collections.abc import bytes_iterator
from itertools import *
k = 0
for n in product (sorted('012345678'), repeat = 5):
    s = ''.join(n)
    if s[0] != '0':
        if int(s[0]) > int(s[1]) > int(s[2]) > int(s[3]) > int(s[4]):
            k+=1
print(k)
42 bit
15 bit
