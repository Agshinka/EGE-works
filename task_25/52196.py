from fnmatch import *
for n in range (0, 10 ** 9, 3127):
    if fnmatch(str(n), '12*93?1?'):
        print(n)