"""
Calculator App

This script allows the user to interact with the methods contained in calc in order to calculate equations of their
choosing in real-time. Using TKinter, it assigns meaning to the UI elements used within this script.

This script requires that 'tkinter' be installed within the Python environment you are running this script in.

"""
from tkinter.ttk import Entry

import calc
from tkinter import *


class CalcUI(LabelFrame):
    """
    The UI for the calculator

    Contains the TKinter elements that create the layout of the calculator, and assigning meaning to
    the buttons, as well as the output.
    """

    def __init__(self):
        super().__init__()
        self.output = Label(self, text='0')
        self.initUI()

    def initUI(self):
        self.master.title("Calculator")

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        cls = Button(self, text="Cls")
        cls.grid(row=1, column=0)

        bck = Button(self, text="Back")
        bck.grid(row=1, column=1)

        lbl = Button(self)
        lbl.grid(row=1, column=2)

        clo = Button(self, text="Close")
        clo.grid(row=1, column=3)

        sev = Button(self, text="7", command=lambda: self.display_number(sev.cget('text')))
        sev.grid(row=2, column=0)

        eig = Button(self, text="8", command=lambda: self.display_number(eig.cget('text')))
        eig.grid(row=2, column=1)

        nin = Button(self, text="9")
        nin.grid(row=2, column=2)

        div = Button(self, text="/")
        div.grid(row=2, column=3)

        fou = Button(self, text="4")
        fou.grid(row=3, column=0)

        fiv = Button(self, text="5")
        fiv.grid(row=3, column=1)

        six = Button(self, text="6")
        six.grid(row=3, column=2)

        mul = Button(self, text="*")
        mul.grid(row=3, column=3)

        one = Button(self, text="1")
        one.grid(row=4, column=0)

        two = Button(self, text="2")
        two.grid(row=4, column=1)

        thr = Button(self, text="3")
        thr.grid(row=4, column=2)

        mns = Button(self, text="-")
        mns.grid(row=4, column=3)

        zer = Button(self, text="0")
        zer.grid(row=5, column=0)

        dot = Button(self, text=".")
        dot.grid(row=5, column=1)

        equ = Button(self, text="=")
        equ.grid(row=5, column=2)

        pls = Button(self, text="+")
        pls.grid(row=5, column=3)

        self.output.grid(row=0, columnspan=4, sticky=W + E)

        self.pack()


def display_number(str):
    """ Changes the output display

    :param str: the same one as the text of the button which is pressed
    :return: the string value (for testing purposes)
    """
    text = CalcUI().output.cget('text')
    newstr = ''
    if text == '' or text == '0':
        newstr = str
    else:
        newstr = text+str
    CalcUI().output.config(text=newstr)
    return newstr

def main():
    root = Tk()
    app = CalcUI()
    root.mainloop()


if __name__ == '__main__':
    main()


