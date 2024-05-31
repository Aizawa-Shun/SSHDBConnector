import tkinter as tk
from tkinter import ttk

class GUI:
    """
    A GUI class that provides a date input form using Tkinter.
    This class allows the user to input a date and makes it available externally.

    Attributes:
        date (str): Holds the date entered by the user.
        root (tk.Tk): The root window of this GUI.
        entry_text (tk.StringVar): String variable bound to the entry widget.
        entry (ttk.Entry): Text input box for entering the date.
        submit_button (ttk.Button): Button to submit the input data.
    """
    def __init__(self, root):
        self.date = ''

        self.root = root
        root.title('Date Selection')
        root.geometry('300x200')

        self.entry_text = tk.StringVar()  # Variable to manage the content of the text box

        # Configure the text input box
        self.entry = ttk.Entry(root, textvariable=self.entry_text, width=30)
        self.entry.pack(padx=30, pady=40, anchor='center')
        
        # Set the placeholder
        self.placeholder = '2024/04'
        self.entry.insert(0, self.placeholder)
        self.entry.config(foreground='grey')
        self.entry.bind('<FocusIn>', self.on_focus_in)
        self.entry.bind('<FocusOut>', self.on_focus_out)

        # Configure the submit button
        self.submit_button = ttk.Button(root, text='Submit', command=self.submit)
        self.submit_button.pack(pady=20, anchor='center')

    def on_focus_in(self, event):
        """
        Event handler when the text box gains focus.
        Clears the placeholder text and sets the text color to black.

        Parameters:
            event: Focus-in event information.
        """
        if self.entry.get() == self.placeholder:
            self.entry.delete(0, tk.END)  # Clear the placeholder
            self.entry.config(foreground='black')

    def on_focus_out(self, event):
        """
        Event handler when the text box loses focus.
        If the user did not enter anything, re-displays the placeholder.

        Parameters:
            event: Focus-out event information.
        """
        if not self.entry.get():
            self.entry.insert(0, self.placeholder)  # Display the placeholder
            self.entry.config(foreground='grey')

    def submit(self):
        """
        Event handler when the submit button is clicked.
        Saves the entered data to the date attribute and closes the window.
        """
        input_value = self.entry.get()
        if input_value != self.placeholder:
            self.date = input_value
        self.root.quit()  # Close the window
