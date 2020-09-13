from tkinter import *
from tkinter import ttk
from tkinter import Menu
import time

# Creates window and defines properties
window = Tk()
window.title("Python Tomato Timer v0.1")
window.geometry("400x200")

#Button Functions go here
def clicked():
    print("click!")

#Countdown timer
def timer():
    initial_time = 1500
    while initial_time != 0:
            minutes, seconds = divmod(initial_time, 60)
            clock = "{:02d}:{:02d}".format(minutes, seconds)
            print(clock)
            time.sleep(1)
            initial_time = initial_time - 1

# Buttons here
start = Button(window, text="Start", bg="grey", fg="white", command=start)
start.grid(column=2, row=2)

stop = Button(window, text="Stop", bg="grey", fg="white", command=clicked)
stop.grid(column=4, row=2)

reset = Button(window, text="Reset", bg="grey", fg="white", command=clicked)
reset.grid(column=6, row=2)


window.mainloop()
