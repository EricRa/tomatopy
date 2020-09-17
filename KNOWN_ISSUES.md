# Known Issues:

- Multiple presses of start cause the function to run multiple times, doubling the speed of the clock.

- Console pops up separate from tkinter app when running script.  Need to hide this.


# Resolved Issues:

- Clock goes into negative time instead of reaching zero instead of stopping the loop
    - *Resolved 9-17-20 1:30 PM*

- Reset timer properly resets the clock internally but does not properly update the UI clock
    - *Resolved 9-17-20 1:45 PM*