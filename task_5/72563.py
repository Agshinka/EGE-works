b=[]
for n in [567_891_233, 567_891_234]:
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '11' + s
    else:
        s = '1' + s + '10'
    r = int(s,2)
    b.append(r)
print(max(b))