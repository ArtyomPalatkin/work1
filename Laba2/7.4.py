import random
x=int(input('Компьютер загадал чилсо от 1 до 3,попытайтесь его угадать'))
if x==random.randint(1,3):
        print('Вы угадали')
else:
        print('Вы не угадали')
