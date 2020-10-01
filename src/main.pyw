from tkinter import *
from tkinter import ttk
from tkinter import Menu

# Creates window and defines properties
root = Tk()
root.title("Python Tomato Timer v0.1")
root.geometry("500x300")
root.config(background="black")

#Countdown timer and button functions

clock = "25:00"
time_label = Label(root, text = clock)
time_label.place(x=150, y=138)
time_label.config(font=("Courier", 50, "bold"))
time_label.config(background="black", foreground="white")

decrement_timer = True
initial_time = 1500

def main_timer():
    global initial_time
    if initial_time == -1:
        stop_timer()
    if not decrement_timer:
        return
    minutes, seconds = divmod(initial_time, 60)
    clock = "{:02d}:{:02d}".format(minutes, seconds)
    time_label.configure(text=clock)
    initial_time = initial_time - 1
    root.after(1000, main_timer)    

def start_timer():   
    global decrement_timer
    if decrement_timer == False:
        decrement_timer = True
        main_timer()

def stop_timer():
    global decrement_timer
    decrement_timer = False

def reset_timer():
    global decrement_timer
    decrement_timer = False
    global initial_time
    initial_time = 1500
    global clock
    time_label.configure(text=clock)

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
