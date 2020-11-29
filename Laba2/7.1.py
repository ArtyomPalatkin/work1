import math
a,b,c=map(int,input('Введите a,b,c').split())
p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print(s)
