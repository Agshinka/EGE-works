with open('files/59702.txt', 'r') as file:
    a = file.readline()
    a = a.split('Y')
    maxx=0
    for n in range (len(a)-150):
        b = 'Y'.join(a[n:n+151])
        if maxx < len(b):
            maxx = len(b)
print(maxx)