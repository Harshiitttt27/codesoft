from tkinter import *


def click(event):
    global value
    text = event.widget.cget("text")

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()

root.config(bg="white")
root.maxsize(744, 900)
root.minsize(644, 700)


scvalue = StringVar()
scvalue.set("")
screen = Entry(
    root, textvariable=scvalue, font="melbourne 40 bold", bg="black", fg="orange"
)
screen.pack(padx=10, pady=10)

frame1 = Frame(root)
button1 = Button(frame1, text="C", font="Melbourne 25 bold", bg="orange")
button1.pack(side=LEFT, padx=15, pady=10)
button1.bind("<Button-1>", click)

button2 = Button(frame1, text="+", font="Melbourne 25 bold", bg="orange")
button2.pack(side=LEFT, padx=15, pady=10)
button2.bind("<Button-1>", click)

button3 = Button(frame1, text="%", font="Melbourne 25 bold", bg="orange")
button3.pack(side=LEFT, padx=15, pady=10)
button3.bind("<Button-1>", click)

frame1.pack()


frame1 = Frame(root)
button4 = Button(frame1, text="7", font="Melbourne 25 bold", bg="white")
button4.pack(side=LEFT, padx=15, pady=10)
button4.bind("<Button-1>", click)

button5 = Button(frame1, text="8", font="Melbourne 25 bold", bg="white")
button5.pack(side=LEFT, padx=15, pady=10)
button5.bind("<Button-1>", click)

button6 = Button(frame1, text="9", font="Melbourne 25 bold", bg="white")
button6.pack(side=LEFT, padx=15, pady=10)
button6.bind("<Button-1>", click)

frame1.pack()


frame1 = Frame(root)
button7 = Button(frame1, text="4", font="Melbourne 25 bold", bg="white")
button7.pack(side=LEFT, padx=15, pady=10)
button7.bind("<Button-1>", click)

button8 = Button(frame1, text="5", font="Melbourne 25 bold", bg="white")
button8.pack(side=LEFT, padx=15, pady=10)
button8.bind("<Button-1>", click)

button9 = Button(frame1, text="6", font="Melbourne 25 bold", bg="white")
button9.pack(side=LEFT, padx=15, pady=10)
button9.bind("<Button-1>", click)

frame1.pack()


frame1 = Frame(root)
button10 = Button(frame1, text="1", font="Melbourne 25 bold", bg="white")
button10.pack(side=LEFT, padx=15, pady=10)
button10.bind("<Button-1>", click)

button11 = Button(frame1, text="2", font="Melbourne 25 bold", bg="white")
button11.pack(side=LEFT, padx=15, pady=10)
button11.bind("<Button-1>", click)

button12 = Button(frame1, text="3", font="Melbourne 25 bold", bg="white")
button12.pack(side=LEFT, padx=15, pady=10)
button12.bind("<Button-1>", click)

frame1.pack()


frame1 = Frame(root)
button13 = Button(frame1, text="0", font="Melbourne 25 bold", bg="white")
button13.pack(side=LEFT, padx=15, pady=10)
button13.bind("<Button-1>", click)

button14 = Button(frame1, text="=", font="Melbourne 25 bold", bg="orange")
button14.pack(side=LEFT, padx=15, pady=10)
button14.bind("<Button-1>", click)

button15 = Button(frame1, text="*", font="Melbourne 25 bold", bg="orange")
button15.pack(side=LEFT, padx=15, pady=10)
button15.bind("<Button-1>", click)

frame1.pack()


frame1 = Frame(root)
button16 = Button(
    frame1, text="C", font="Melbourne 25 bold", bg="orange", relief=SUNKEN
)
button16.pack(side=LEFT, padx=15, pady=10)
button16.bind("<Button-1>", click)

button17 = Button(frame1, text="/", font="Melbourne 25 bold", bg="orange")
button17.pack(side=LEFT, padx=15, pady=10)
button17.bind("<Button-1>", click)

button18 = Button(frame1, text=".", font="Melbourne 25 bold", bg="orange")
button18.pack(side=LEFT, padx=15, pady=10)
button18.bind("<Button-1>", click)

frame1.pack()

root.title("My calculator")

root.mainloop()
