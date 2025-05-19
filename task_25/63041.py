from fnmatch import *
for n in range (0, 10 ** 10, 3147):
    if fnmatch(str(n), '1*4302?1'):
        print(n)