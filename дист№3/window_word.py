import tkinter
import random
window = tkinter.Tk()
words={"собака":"dog","мужчина":"man","женщина":"woman","кошка":"cat"}
list=["собака","мужчина","женщина","кошка"]
a=random.choice(list)
label = tkinter.Label(window, text="Случайное слово:")
label.pack()
label1=tkinter.Label(window,text=words[a])
label1.pack()
label2=tkinter.Label(window,text="Укажите перевод слова:")
label2.pack()
var = tkinter.StringVar()
entry = tkinter.Entry(window, textvariable=var)
entry.pack()
def click():
        if entry.get()==a:
            label3 = tkinter.Label(window, text="Угадали")
            label3.pack()
button = tkinter.Button(window, text='Click', command=click)
button.pack()






window.mainloop()
