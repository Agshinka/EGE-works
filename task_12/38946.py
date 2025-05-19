b=[]
for n in range(200, 500):
    s = '1' * n
    while '111' in s or '222' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '1', 1)
    if '2' not in s:
        print(n)
        break