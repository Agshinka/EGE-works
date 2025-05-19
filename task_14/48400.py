a = '0123456789a'
for x in a:
    d = int('95' + x + '2', 11) + int(x + '458', 12)
    if d % 136 == 0:
        print((d / 136))