"""Calculator App

This script allows the user to interact with the methods contained in calc in order to calculate equations of their
choosing in real-time. Using TKinter, it assigns meaning to the UI elements used within this script.

This script requires that 'tkinter' be installed within the Python environment you are running this script in.

"""
import calc
from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry("400x400")


class CalcUI:
    """
    The UI for the calculator

    Contains the TKinter elements that create the layout of the calculator, and assigning meaning to
    the buttons, as well as the output.
    """
    def __init__(self, main):
        buttonFrame = Frame(main)
        buttonFrame.pack()

root.mainloop()