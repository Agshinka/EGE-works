from fnmatch import *
for n in range (0, 10 ** 10, 4173):
    if fnmatch(str(n), '1?2655*8'):
        print(n)