b=[]
for n in range (60, 500):
    s = '1' * n
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '11', 1)
    if s == '2211':
        print(n)
        break