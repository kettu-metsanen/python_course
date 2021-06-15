"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""

from tkinter import *


class Counter:
    def __init__(self):
        # TODO: You have to creater one label and four buttons and store
        #       them in the following attributes:
        #
        #       self.__current_value    # Label displaying the current value of the counter.
        #       self.__reset_button     # Button which resets counter to zero.
        #       self.__increase_button  # Button which increases the value of the counter by one.
        #       self.__decrease_button  # Button which decreases the value of the counter by one.
        #       self.__quit_button      # Button which quits the program.
        #
        #       Make sure you name the components exactly as shown above,
        #       otherwise the automated tests will fail.

        self.__pääikkuna = Tk()
        self.__text = 0
        self.__current_value = Label(self.__pääikkuna, text=self.__text)
        self.__current_value.grid(row=0, column=0, columnspan=5)
        self.__reset_button = Button(self.__pääikkuna, text="Reset",
                                  command=self.reset)
        self.__reset_button.grid(row=1, column=0)
        self.__increase_button = Button(self.__pääikkuna, text="Increase",
                                  command=self.increase)
        self.__increase_button.grid(row=1, column=2)
        self.__decrease_button = Button(self.__pääikkuna, text="Decrease",
                                  command=self.decrease)
        self.__decrease_button.grid(row=1, column=3)
        self.__quit_button = Button(self.__pääikkuna, text="Quit",
                                  command=self.lopeta)
        self.__quit_button.grid(row=1, column=4)
        self.__pääikkuna.mainloop()
        
    def lopeta(self):
        self.__pääikkuna.destroy()
    
    def increase(self):
        self.__text += 1
        self.__current_value.configure(text = self.__text)
    def decrease(self):
        self.__text -= 1
        self.__current_value.configure(text = self.__text)
    def reset(self):
        self.__text = 0
        self.__current_value.configure(text = self.__text)
    # TODO: Implement the rest of the needed methods here.


def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()
