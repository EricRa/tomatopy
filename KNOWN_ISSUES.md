# Known Issues:



# Resolved Issues:

- Clock goes into negative time instead of reaching zero instead of stopping the loop
    - Resolved 9-17-20 1:30 PM

- Reset timer properly resets the clock internally but does not properly update the UI clock
    - Resolved 9-17-20 1:45 PM
    
- Console pops up separate from tkinter app when running script.  Need to hide this.
    - Resolved 9-18-20 2:00PM
    - Note: This issue can be prevented by invoking the pythonw executable.  This is most easily done by saving the main script file with a .pyw extention instead of a a .py one.*

- Multiple presses of start cause the function to run multiple times, doubling the speed of the clock.
    - Resolved 10-1-30 5:00PM
    - Fixed by changing start_timer() function to only run if decrement_timer is currently False