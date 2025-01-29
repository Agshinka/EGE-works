a = '0123456789abcde'
for x in a:
    d = int(x + 'B09', 17) + int(x + '8E8', 15)
    if d % 155 == 0:
        print(int(d//155))