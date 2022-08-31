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

        clr = Button(self, text="Clr", command=lambda: self.clear())
        clr.grid(row=1, column=0)

        delete = Button(self, text="Delete", command=lambda: self.delete(self.output.cget('text')))
        delete.grid(row=1, column=1)

        lbl = Button(self)
        lbl.grid(row=1, column=2)

        clo = Button(self, text="Close", command=lambda: self.close_application())
        clo.grid(row=1, column=3)

        sev = Button(self, text="7", command=lambda: self.display_number(sev.cget('text')))
        sev.grid(row=2, column=0)

        eig = Button(self, text="8", command=lambda: self.display_number(eig.cget('text')))
        eig.grid(row=2, column=1)

        nin = Button(self, text="9", command=lambda: self.display_number(nin.cget('text')))
        nin.grid(row=2, column=2)

        div = Button(self, text="/", command=lambda: self.divide(self.output.cget('text')))
        div.grid(row=2, column=3)

        fou = Button(self, text="4", command=lambda: self.display_number(fou.cget('text')))
        fou.grid(row=3, column=0)

        fiv = Button(self, text="5", command=lambda: self.display_number(fiv.cget('text')))
        fiv.grid(row=3, column=1)

        six = Button(self, text="6", command=lambda: self.display_number(six.cget('text')))
        six.grid(row=3, column=2)

        mul = Button(self, text="*")
        mul.grid(row=3, column=3)

        one = Button(self, text="1", command=lambda: self.display_number(one.cget('text')))
        one.grid(row=4, column=0)

        two = Button(self, text="2", command=lambda: self.display_number(two.cget('text')))
        two.grid(row=4, column=1)

        thr = Button(self, text="3", command=lambda: self.display_number(thr.cget('text')))
        thr.grid(row=4, column=2)

        mns = Button(self, text="-")
        mns.grid(row=4, column=3)

        zer = Button(self, text="0", command=lambda: self.display_number(zer.cget('text')))
        zer.grid(row=5, column=0)

        dot = Button(self, text=".",
                     command=lambda: self.display_special_character(dot.cget('text'),self.output.cget('text')))
        dot.grid(row=5, column=1)

        equ = Button(self, text="=", command=lambda: self.equals(self.output.cget('text')))
        equ.grid(row=5, column=2)

        pls = Button(self, text="+", command=lambda:self.add_button(self.output.cget('text')))
        pls.grid(row=5, column=3)

        self.output.grid(row=0, columnspan=4, sticky=W + E)

        self.pack()

    def check_for_undefined(self):
        """ Helper method to check if the output label contains the word 'Undefined'

        :return: true if output contains word Undefined, otherwise false
        """
        if "Undefined" in self.output.cget("text"):
            return True
        else:
            return False

    def add_button(self,button_text):
        """ Includes functionality for updating display when + is pressed

        :param str: the text displayed on the button this method is attached to
        :return: string representation of output's text
        """

        text = button_text
        newtext = text + " + "
        self.output.config(text=newtext)
        return newtext

    def divide(self,button_text):
        """ Includes functionality for updating display when / is pressed

        :param button_text: the text displayed on the button this method is attached to
        :return: string representation of output's text
        """
        text = button_text
        newText = text + " / "
        self.output.config(text=newText)
        return newText

    def equals(self, equation_string):
        """ When pressed this should update the display with all of the calculations waiting in output label

        That means we need to strip the string that this method receives

        :param equation_string: the string that is shown in the output label of the calc before the user hits = sign
        :return: string representation of output's text
        """
        stripped_equation = list(equation_string.replace(" ", ""))
        prevNum = 1
        prevNumString = ''
        nextNum = 1
        for element in range(0, len(stripped_equation)):

            if stripped_equation[element] == '/':
                nextNum = int(stripped_equation[element + 1])                       # check for zero division
                if nextNum == 0:
                    self.output.config(text="Undefined")                            # show error to user and exit loop
                    return self.output.cget('text')
                count = element

                while stripped_equation[count - 1].isnumeric() and count-1 >= 0:
                    prevNumString += stripped_equation[count-1]
                    count -= 1

                if stripped_equation[element+1]:
                    prevNumString = prevNumString[::-1]
                    prevNum = int(prevNumString)

                    newNumber = float(calc.divide(prevNum,nextNum))
                    self.output.config(text=str(newNumber))

                    return str(newNumber)
        return ""

    def clear(self):
        """ When pressed this should update the output with a blank string

        :return: string representation of the number 0, since 0 should be the default display
        """
        self.output.config(text='0')
        return self.output.cget('text')

    def delete(self, str):
        """ When the delete button is pressed, this method should remove a single text character from the screen

        Order matters for this, if delete is pressed, only the most recently added text item should be removed, and if
        it is pressed again, then the one before that should be removed, and so on.

        return: string, the output label's text after deleting a char
        """

        text = str
        text = text[:-1]
        if text[-1] == " ":
            text = text[:-1]
        if text[-1] == ".":
            text = text[:-1]
        self.output.config(text=text)
        return text

    def display_number(self,str):
        """ Changes the output display

        :param str: the same one as the text of the button which is pressed
        :return: the string value (for testing purposes)
        """
        text = self.output.cget('text')
        newstr = ''
        if text == '' or text == '0' or self.check_for_undefined():
            newstr = str
        else:
            newstr = text+str
        self.output.config(text=newstr)
        return newstr

    def display_special_character(self, specChar, strToChange):
        """ Changes the output display, making sure that special characters don't get repeated

        :poram: specChar: the same one as the text of the button which is pressed
        :param: strToChange: the string we want to add a char to
        :return: the string value (for testing purposes)
        """
        if strToChange[-1] == specChar:
            return strToChange
        strToChange += specChar
        self.output.config(text=strToChange)
        return self.output.cget('text')

    def close_application(self):
        global root                     # Meed to grab the global instance of the application window
        root.destroy()


root = Tk()                             # Need this outside of main function in order to access and close the window
app = CalcUI()


def main():
    root.mainloop()


if __name__ == '__main__':
    main()


