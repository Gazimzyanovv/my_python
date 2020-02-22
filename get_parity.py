number=input("Введите число и я скажу четное ли оно\n")
if number:
    num=float(number)
    num=num/2
    if int(num)==float(num):
        print("True")
    else:
        print("False")
