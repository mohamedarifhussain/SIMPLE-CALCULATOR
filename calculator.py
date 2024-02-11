from tkinter import *

values =[]

window = Tk()
window.config(padx=20,pady=20,bg="black")

entry_box = Entry(window)
entry_box.grid(row=0,column=0,columnspan=5)

label = Label(bg="black")
label.grid(row=1,column=0,columnspan=3)

button_1 = Button(text="1",width=2,command=lambda : number('1'))
button_1.grid(row=2,column=0)

button_2 = Button(text="2",width=2,command=lambda : number('2'))
button_2.grid(row=2,column=1)

button_3 = Button(text="3",width=2,command=lambda : number('3'))
button_3.grid(row=2,column=2)

button_4 = Button(text="4",width=2,command=lambda : number('4'))
button_4.grid(row=3,column=0)

button_5 = Button(text="5",width=2,command=lambda : number('5'))
button_5.grid(row=3,column=1)

button_6 = Button(text="6",width=2,command=lambda : number('6'))
button_6.grid(row=3,column=2)

button_7 = Button(text="7",width=2,command=lambda : number('7'))
button_7.grid(row=4,column=0)

button_8 = Button(text="8",width=2,command=lambda : number('8'))
button_8.grid(row=4,column=1)

button_9 = Button(text="9",width=2,command=lambda : number('9'))
button_9.grid(row=4,column=2)

button_0 = Button(text="0",width=2,command=lambda : number('0'))
button_0.grid(row=5,column=1)

button_add = Button(text="+",width=2,command=lambda : save("+"))
button_add.grid(row=2,column=3)

button_sub = Button(text="-",width=2,command=lambda : save("-"))
button_sub.grid(row=3,column=3)

button_mul = Button(text="*",width=2,command=lambda : save("*"))
button_mul.grid(row=4,column=3)

button_div = Button(text="/",width=2,command=lambda : save("/"))
button_div.grid(row=5,column=3)

button_dot = Button(text=".",width=2,command=lambda : number('.'))
button_dot.grid(row=5,column=0)

button_equal = Button(text="=",width=2,command=lambda : save("="))
button_equal.grid(row=5,column=2)




def number(num:str):
    entry_box.insert(END,num)


def all_clear():
    global values,operator
    entry_box.delete(0,END)
    values=[]
    operator=""

def off():
    window.destroy()

button_ac = Button(text="AC",width=7,command=all_clear)
button_ac.grid(row=6,column=0,columnspan=2)

button_off = Button(text="off",width=7,command=off)
button_off.grid(row=6,column=2,columnspan=2)


def save(op:str):
    global values, operator
    if op!="=":
        operator=op
    if values == []:
        values.append(float(entry_box.get()))
        # print(values)
        entry_box.delete(0,END)
        return
    else:
        if operator=="+":
            values[len(values)-1]+=float(entry_box.get())
        elif operator[0]=="-":
            values[len(values)-1]-=float(entry_box.get())
        elif operator[0]=="*":
            values[len(values)-1]*=float(entry_box.get())
        elif operator[0]=="/":
            values[len(values)-1]/=float(entry_box.get())

        entry_box.delete(0, END)
        if op=="=":
            entry_box.insert(0, str(values[0]))
        # print(values)


window.mainloop()
