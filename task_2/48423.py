print('x y z w f')
for x in range (2):
    for y in range (2):
        for z in range (2):
            for w in range (2):
                if ((x <= (y == w)) and (y == (w <= z))):
                    print(x, y, z, w, 1)
                if not((x <= (y == w)) and (y == (w <= z))):
                    print(x, y, z, w, 0)