#This is a random password generator which is made in python using tkinter
#It ask user that what type of password user wants ie; weak password/average or strong
#It also ask user about the password length

import string
import random
from tkinter import *


def select():
    select = choice.get()


def callback():
    final.config(text=passgen())


def passgen():
    if choice.get() == 1:
        return "".join(random.sample(weak, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    else:
        return "".join(random.sample(strong, val.get()))


root = Tk()

root.config(bg="beige")

root.geometry("444x522")
root.maxsize(344, 422)

L = Label(
    text="Password generator using python",
    font="Lucida 15 italic",
    relief=SUNKEN,
    bg="green",
    fg="white",
)
L.pack()

choice = IntVar()

r1 = Radiobutton(
    root,
    text="Weak password",
    bg="red",fg="white", font="lucida 20",
    variable=choice,
    value=1,
    activebackground="yellow",
    activeforeground="black",
)
r1.pack(pady=15, padx=10)
r2 = Radiobutton(
    root,
    text="Average password",
    bg="red",fg="white",
    variable=choice,font="lucida 20",
    value=2,
    activebackground="yellow",
    activeforeground="black",
)
r2.pack(pady=15, padx=10)
r3 = Radiobutton(
    root,
    text="Strong password",
    bg="red",fg="white",font="lucida 20",
    variable=choice,
    value=3,
    activebackground="yellow",
    activeforeground="black"
)
r3.pack(pady=15, padx=10)

val = IntVar()
spinlength = Spinbox(root, from_=6, to_=10, font="lucida 10",textvariable=val, width=20)
spinlength.pack(pady=10)

submit = Button(root,text="GENERATE PASSWORD",pady=9,padx=8,font="Lucida 9 bold", bg="green",fg="beige",
    command=callback).pack()

weak = string.ascii_lowercase + string.digits
average = string.ascii_lowercase + string.ascii_uppercase + string.digits
strong = (
    string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
)

final = Message(root, text="",font="lucida 15", relief=SUNKEN,bg="black",fg="beige",width=45)
final.pack(padx=20,pady=5)

root.mainloop()
