s = '7' * 108
while '3333' in s or '777' in s:
    if '33333' in s:
        s = s.replace ('33333', '7', 1)
    else:
        s = s.replace ('777', '3', 1)
print(s)