print('x y z w f')
for x in range (2):
    for y in range (2):
        for z in range (2):
            for w in range (2):
                if (z == (x <= w)) and (x == (not(w <= y))):
                    print(x, y, z, w, 1)
                if not((z == (x <= w)) and (x == (not(w <= y)))):
                    print(x, y, z, w, 0)
