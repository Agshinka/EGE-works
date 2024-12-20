for n in range (100, 1000000):
    s = str(n)       
    b=[]
    while len(s) >= 3:            
        b.append(int(s[:3]))          # Обрезает (с начала до 3го индекса)
        s = s[1:]                     # Сдвигает вправо
        r = max(b) - min(b)       
    if r == 623:                      # Ну и по условию идем
        print(n)
        break