with open('files/68257.txt' , 'r') as file:
    a = file.readline()
    b = sorted(list(set(a)))[:13]
    s = 0
    maxx = 0
    for n in b:
        maxx = max(maxx, len(max(a.split(n), key = len)) + 2)
print(maxx)