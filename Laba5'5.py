def cost(k,s):
    if k==343:
            x=15
    elif k==341:
            x=18
    elif k==485:
            x=1
    elif k==473:
            x=13
    return s*x
print("Введите код города")
k=int(input())
print("Введите длительность")
s=int(input())
print("Стоимость будет равна",cost(k,s))
