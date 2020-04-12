import tkinter
window=tkinter.Tk()
list=[]

l1=tkinter.Label(window,text="Task:")
l1.grid(row=0,column=0)
l2=tkinter.Label(window,text="Category:")
l2.grid(row=1,column=0)
l3=tkinter.Label(window,text="Time:")
l3.grid(row=2,column=0)

e1 = tkinter.Entry(window)
e1.grid(row=0,column=1)
e2 = tkinter.Entry(window)
e2.grid(row=1,column=1)
e3 = tkinter.Entry(window)
e3.grid(row=2,column=1)

def b1():
    list.append({})
    list[len(list)-1]["Task"]=e1.get()
    list[len(list)-1]["Category"]=e2.get()
    list[len(list)-1]["Time"]=e3.get()
def b2():
    for i in list:
        print(i)
def b3():
    window.destroy()

b1= tkinter.Button(window, text='Add', command=b1)
b1.grid(row=3,column=1)
b2= tkinter.Button(window, text='Show list', command=b2)
b2.grid(row=4,column=1)
b3=tkinter.Button(window, text="Exit",command=b3)
b3.grid(row=5,column=1)

window.mainloop()
