from tkinter import *


def sel():
    data = ["Python", "Java", "Angular"]
    res = ""
    i = 0
    for l in li:
        if l.get():
            res += data[i]
        i += 1

    print(fn.get())
    print(passw.get())
    if var.get()==1:
        print("M")
    else:
        print("F")
    print(res)


tkit = Tk()
fn = StringVar()
L1 = Entry(tkit, text="First Name", textvariable=fn)
L1.pack(side=TOP)
passw= StringVar()
L2 = Entry(tkit, text="password",textvariable=passw)
L2.pack(side=TOP)

var = IntVar()  # The Variable Classes (BooleanVar, DoubleVar, IntVar, StringVar)
R1 = Radiobutton(tkit, text="Male", variable=var, value=1,
                 )
R1.pack()
R2 = Radiobutton(tkit, text="Female", variable=var, value=2
                 )
R2.pack()

li = [IntVar(), IntVar(), IntVar()]
label = Label(tkit)

C1 = Checkbutton(tkit, text="Python", variable=li[0],
                 onvalue=1, offvalue=0, height=5,
                 width=20)
C2 = Checkbutton(tkit, text="Angular", variable=li[1],
                 onvalue=1, offvalue=0, height=5,
                 width=5)
C3 = Checkbutton(tkit, text="React", variable=li[2],
                 onvalue=1, offvalue=0, height=5,
                 width=5)
C1.pack()
C2.pack()
C3.pack()
E1 = Button(tkit, bd=5, text='Submit', command=sel)
E1.pack(side=BOTTOM)

label.pack()

tkit.mainloop()