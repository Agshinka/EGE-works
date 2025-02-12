with open('files/29674.txt', 'r') as file:
    a = file.readlines()
    kolvo = a[0]
    kolvo = int(kolvo)
    del a[0]
    price = sorted([int(i) for i in a])
    minn = []
    for g in range (len(price)):
        if price[g] <= 50:
            minn.append(price[g])
        else:
            price = price[g:]
            break
    mostex = max(price[:482])
    discount = sum(price[:482]) - ((sum(price[:482]) // 100) * 25)
    nodiscount = sum(price[482:]) + sum(minn)
    print(nodiscount + discount, mostex)