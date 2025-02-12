with open('files/33105.txt', 'r') as file:
    a = file.readlines()
    kolvo = a[0]
    kolvo = int(kolvo)
    del a[0]
    price = sorted([int(i) for i in a])
    minn = []
    for n in range (len(price)):
        if price[n] <= 100:
            minn.append(price[n])
        else:
            price = price[n:]
            break
    mostex = max(price[:453])
    discount = sum(price[:453]) - (sum(price[:453]) * 0.3)
    nodiscount = sum(price[453:]) + sum(minn)
    print(discount + nodiscount, mostex)