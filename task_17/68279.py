with open('files/68279.txt', 'r') as file:
    a = file.readlines()
    a = [int(i) for i in a]
    k = 0
    b = []
    g = []
    s = []
    for j in range (len(a)):

        if a[j] % 1000 == 562:

            g.append(a[j])

    for n in range (len(a)-3):
        suma = a[n] + a[n+1] + a[n+2] + a[n+3]

        q = [a[n], a[n+1], a[n+2], a[n+3]]

        qlen = [len(str(j)) for j in q]

        if f'{qlen[0]}{qlen[1]}{qlen[2]}{qlen[3]}'.count('5') <= 2 and '5' in f'{qlen[0]}{qlen[1]}{qlen[2]}{qlen[3]}':

            d3 = len([k for k in q if k % 3 == 0])

            d7 = len([t for t in q if t % 7 == 0])

            if d7 > d3:

                if (suma > max(g)) and (suma < (max(g) * 2)):

                    b.append(a[n] + a[n+1] + a[n+2] + a[n+3])

                    k+=1
print(k, max(b))