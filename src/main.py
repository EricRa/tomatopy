from tkinter import *
from tkinter import ttk
from tkinter import Menu
import time

# Creates window and defines properties
root = Tk()
root.title("Python Tomato Timer v0.1")
root.geometry("500x300")
root.config(background="black")

#Button Functions go here
def clicked():
    print("click!")

#Countdown timer and button functions

clock = int(1500)
time_label = Label(root, text = clock)
time_label.place(x=150, y=138)
time_label.config(font=("Courier", 50, "bold"))
time_label.config(background="black", foreground="white")
    
def start_timer():   
    initial_time = 1500
    while initial_time != 0:
            minutes, seconds = divmod(initial_time, 60)
            clock = "{:02d}:{:02d}".format(minutes, seconds)
            time_label.grid()
            time.sleep(1)
            initial_time = initial_time - 1

def stop_timer():
    pass

def reset_timer():
    pass

# Buttons here
start = Button(root, text="Start", bg="grey", fg="white", command=start_timer)
start.grid(column=2, row=2)
start.config(font=("Courier", 34))
start.config(background = "green", foreground = "white")

stop = Button(root, text="Stop", bg="grey", fg="white", command=stop_timer)
stop.grid(column=4, row=2)
stop.config(font=("Courier", 34))
stop.config(background = "red", foreground = "white")

reset = Button(root, text="Reset", bg="grey", fg="white", command=reset_timer)
reset.grid(column=6, row=2)
reset.config(font=("Courier", 34))
reset.config(background = "#a8b548", foreground = "white")


root.mainloop()
