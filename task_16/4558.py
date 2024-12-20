#ПРИМЕР
# def getname():
#     name = input('Ваше имя?\n')
#     if len(name) < 2 or not name.isalpha():
#         return getname()
#     else:
#         return name

# print(getname())

def fun(n):
    if n == 1:
        return 1
    else:
        return fun(n-1)*n 
print(fun(5))