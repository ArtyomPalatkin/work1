print("Введите вашу массу")
m=int(input())
print("Введите ваш рост")
h=float(input())
I=m/(h*h)
print("BMI - величина, позволяющая оценить степень соответствия массы человека и его роста и тем самым косвенно судить о том, является ли масса недостаточной, нормальной или избыточной. Важен при определении показаний для необходимости лечения.")
if I<16:
    print("Выраженный дефицит массы тела")
elif 16 <= I < 18.5:
    print("Недостаточная (дефицит) масса тела")
elif 18.5 <= I < 25:
    print("Норма")
elif 25 <= I < 30:
    print("Избыточная масса тела (предожирение)")
elif 30 <= I < 35:
    print("Ожирение")
elif 35 <= I < 40:
    print("Ожирение резкое")
elif I>40:
    print("Очень резкое ожирение")