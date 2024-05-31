import tkinter as tk
import gui

def display():
    '''
    Displays the date selection screen using the GUI and returns the date selected by the user.

    This function executes the following steps:
    1. Instantiates the GUI class from gui.py.
    2. Uses Tkinter's mainloop to display the GUI and wait for user input.
    3. When the user selects a date and finishes the selection, the selected date is stored in app.date.

    Returns:
        str: The date selected by the user as a string in the format YYYY/MM/DD.
    '''
    root = tk.Tk() # Create the root instance of the GUI
    app = gui.GUI(root)   # Instantiate the GUI class
    root.mainloop()  # Keep displaying the GUI
    return app.date
