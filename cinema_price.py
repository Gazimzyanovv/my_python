x=float(input("Введите номер фильма: 1.Паразиты 2.1917 3.Соник в кино\n"))
y=float(input("Выберите Дату: 1.Сегодня 2.Завтра\n"))
z=float(input("Выберите время: 1.10:00  2.14:00  3.18:00\n"))
e=float(input("Введите количество билетов\n"))
c=0
if x==1:
    if z==1:
        c=200*e
    elif z==2:
        c=250*e
    elif z==3:
        c=300*e
elif x==2:
    if z==1:
        c=250*e
    elif z==2:
        c=300*e
    elif z==3:
        c=350*e
elif z==3:
    if z==1:
        c=300*e
    elif z==2:
        c=350*e
    elif z==3:
        c=400*e
if y==2:
    c=c*00.5
if e>20:
    c=c*0.8
print(c)
