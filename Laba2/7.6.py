import math
x,y=map(int,input('Введите x,y').split())
z=(x+((2+y)/x**2))/(y + 1/math.sqrt(x**2+10))
q=2.8*math.sin(x)+math.fabs(y)
print (z,q)
