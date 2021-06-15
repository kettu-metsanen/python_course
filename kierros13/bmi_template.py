"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Body Mass Index template
"""

from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()

        # TODO: Create an Entry-component for the weight.
        self.__weight_value = Entry(self.__mainwindow)

        # TODO: Create an Entry-component for the height.
        self.__height_value = Entry(self.__mainwindow)

        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        #       the default colour.
        self.__calculate_button = Button(self.__mainwindow, text="Calculate",
                                  command=self.calculate_BMI)

        # TODO: Create a Label that will show the decimal value of the BMI
        #      after it has been calculated.
        self.__result_text = Label(self.__mainwindow, text= 0)

        # TODO: Create a Label that will show a verbal description of the BMI
        #       after the BMI has been calculated.
        self.__explanation_text = Label(self.__mainwindow, text= "")

        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow, text="Quit",
                                  command=self.stop)

        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        self.__weight_value.grid(row=0, column=0)
        self.__height_value.grid(row=0, column=2)
        self.__calculate_button.grid(row=1, column=1)
        self.__result_text.grid(row=2, column=0, columnspan=3)
        self.__explanation_text.grid(row=3, column=0, columnspan=3)
        self.__stop_button.grid(row=4, column=2)


    # TODO: Implement this method.
    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """
        #ves = 0
        try:
            ves= float(self.__weight_value.get())
            rost= float(self.__height_value.get())
            result = ves / ((rost * rost) / 10000)
            self.__result_text["text"] = '{:.{}f}'.format( result, 2 )
            if result > 18.5 and result < 25:
                self.__explanation_text["text"] = "Your weight is normal."
            elif result > 25:
                self.__explanation_text["text"] = "You are overweight."
            elif result < 18.5:
                self.__explanation_text["text"] = "You are underweight."
            if ves < 0 or rost < 0:
                self.__explanation_text["text"] = "Error: height and weight must be positive."
                self.__result_text["text"] = ""
                self.reset_fields()
        except ValueError:
            self.__explanation_text["text"] = "Error: height and weight must be numbers."
            self.__result_text["text"] = ""
            self.reset_fields()
            

    # TODO: Implement this method.
    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """
        self.__result_text.configure(text = "")
        self.__height_value.delete(0, END)
        self.__weight_value.delete(0, END)

    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
