x=input("Введите вещественное число\n")
if x:
    x=float(x)
    if -2.4<x<5.7:
        x=x**2
        print(x)
    else:
        print(4)
