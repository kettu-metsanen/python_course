"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""

from tkinter import *
import numpy as np


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()
        self.__mainwindow.title("Equation calculator")
        menubar = Menu(self.__mainwindow)
        self.__mainwindow.config(menu=menubar)
        fileMenu = Menu(menubar)
        submenu = Menu(fileMenu)
        submenu.add_command(label="Linear equation", command=self.linear)
        submenu.add_command(label="Quadratic equation", command=self.quadratic)
        submenu.add_command(label="Cubic equation", command=self.cubic)
        submenu2 = Menu(fileMenu)
        submenu2.add_command(label="two equations", command=self.two_system)
        submenu2.add_command(label="tree equations", command=self.tree_system)
        fileMenu.add_cascade(label="linear system of equations", menu=submenu2, underline=0)
        fileMenu.add_cascade(label="Equation", menu=submenu, underline=0)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.stop)
        menubar.add_cascade(label="Equation", menu=fileMenu)
        self.__mode = "cubic"
        self.var = BooleanVar()
        self.cb = Checkbutton(self.__mainwindow, text="Round to tenths", variable=self.var, command=self.round_result)
        self.__cub_entry = Entry(self.__mainwindow, width = 5)
        self.__quadratic_entry = Entry(self.__mainwindow, width = 5)
        self.__one_entry = Entry(self.__mainwindow, width = 5)
        self.__number_entry = Entry(self.__mainwindow, width = 5)
        self.__answer_entry = Entry(self.__mainwindow, width = 5)
        self.__cub_text = Label(self.__mainwindow, text= "x^3 + ")
        self.__quadratic_text = Label(self.__mainwindow, text= "x^2 + ")
        self.__one_x_text = Label(self.__mainwindow, text= "x + ")
        self.__equally_text = Label(self.__mainwindow, text= " = ")
        self.__determenant = Label(self.__mainwindow, text= "D = ")
        self.__answer_x1 = Label(self.__mainwindow, text= "X1 = ")
        self.__answer_x2 = Label(self.__mainwindow, text= "X2 = ")
        self.__answer_x3 = Label(self.__mainwindow, text= "X3 = ")
        self.__error = Label(self.__mainwindow, text= "")
        self.__stop_button = Button(self.__mainwindow, text="Quit",
                                  command=self.stop)
        self.__calculate_button = Button(self.__mainwindow, text="calculate",
                                  command=self.calculate)
        self.__clear_button = Button(self.__mainwindow, text="clear",
                                  command=self.reset_fields)
        
        
        self.__cub_entry.grid(row=1, column=0)
        self.__quadratic_entry.grid(row=1, column=2)
        self.__one_entry.grid(row=1, column=4)
        self.__number_entry.grid(row=1, column=6)
        self.__answer_entry.grid(row=1, column=8)
        self.__cub_text.grid(row=1, column=1)
        self.__quadratic_text.grid(row=1, column=3)
        self.__one_x_text.grid(row=1, column=5)
        self.__equally_text.grid(row=1, column=7)
        self.__answer_x1.grid(row=5, column=1, columnspan=2)
        self.__answer_x2.grid(row=5, column=3, columnspan=2)
        self.__answer_x3.grid(row=5, column=6, columnspan=2)
        self.__error.grid(row=7, column=0, columnspan=8)
        self.__stop_button.grid(row=9, column=8, ipadx = 20)
        self.__calculate_button.grid(row=9, column=0, ipadx = 20)
        self.__clear_button.grid(row=9, column=3, ipadx = 20)
        self.cb.grid(row=6, column=0)
        
        
                          
        self.__mainwindow.mainloop()
    

    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def linear(self):
        
        
        self.__one_entry.grid()
        self.__number_entry.grid()
        self.__answer_entry.grid()
        self.__one_x_text.grid()
        self.__equally_text.grid()
        self.__answer_x1.grid()
        self.cb.grid()
        
        self.reset_fields()
        self.__cub_text.configure(text= "")
        self.__quadratic_text.configure(text= "")
        self.__answer_x2.configure(text= "")
        self.__answer_x3.configure(text= "")
        self.__cub_entry.grid_remove()
        self.__quadratic_entry.grid_remove()
        self.__mode = "linear"
        
    def quadratic(self):
        
        self.__one_entry.grid()
        self.__number_entry.grid()
        self.__answer_entry.grid()
        self.__one_x_text.grid()
        self.__equally_text.grid()
        self.__answer_x1.grid()
        self.__quadratic_text.grid()
        self.__answer_x2.grid()
        self.cb.grid()
        
        self.reset_fields()
        self.__cub_text.configure(text= "")
        self.__quadratic_text.configure(text= "x^2 + ")
        self.__answer_x2.configure(text= "X2 = ")
        self.__answer_x3.configure(text= "")
        self.__quadratic_entry.grid()
        self.__cub_entry.grid_remove()
        self.__mode = "square"
        
    def cubic(self):

        self.__one_entry.grid()
        self.__number_entry.grid()
        self.__answer_entry.grid()
        self.__one_x_text.grid()
        self.__equally_text.grid()
        self.__answer_x1.grid()
        self.__quadratic_text.grid()
        self.__cub_text.grid()
        self.__answer_x2.grid()
        self.__answer_x3.grid()
        self.cb.grid()        

        self.reset_fields()
        self.__cub_text.configure(text= "x^3 + ")
        self.__quadratic_text.configure(text= "x^2 + ")
        self.__answer_x2.configure(text= "X2 = ")
        self.__answer_x3.configure(text= "X3 = ")
        self.__quadratic_entry.grid()
        self.__cub_entry.grid()
        self.__mode = "cubic"
        
    def calculate(self):
        try:
            if self.__mode == "cubic":
                self.__error.configure(text = "")
                try:
                    x3 = float(self.__cub_entry.get())
                    x2 = float(self.__quadratic_entry.get())
                    x = float(self.__one_entry.get())
                    number = float(self.__number_entry.get())
                    answer = float(self.__answer_entry.get())
                    if answer != 0:
                        number = number + (-answer)
                        answer = 0
                    result = np.roots([x3,x2,x,number])
                    self.root1 = result[0]
                    self.root2 = result[1]
                    self.root3 = result[2]
                    self.__answer_x1.configure(text= f"X1 = {self.root1}")
                    self.__answer_x2.configure(text= f"X2 = {self.root2}")
                    self.__answer_x3.configure(text= f"X3 = {self.root3}")
                    if self.var.get():
                        self.round_result()
                except IndexError:
                    self.__error.configure(text = "Error: ne mojet bit ravno nulu")
                
            if self.__mode == "square":
                self.__error.configure(text = "")
                try:
                    x2 = float(self.__quadratic_entry.get())
                    x = float(self.__one_entry.get())
                    number = float(self.__number_entry.get())
                    answer = float(self.__answer_entry.get())
                    if answer != 0:
                        print("and here")
                        number = number + (-answer)
                        answer = 0
                    result = np.roots([x2,x,number])
                    self.root1 = result[0]
                    self.root2 = result[1]
                    self.__answer_x1.configure(text= f"X1 = {self.root1}")
                    self.__answer_x2.configure(text= f"X2 = {self.root2}")
                    if self.var.get():
                        self.round_result()
                except IndexError:
                    self.__error.configure(text = "Error: ne mojet bit ravno nulu")
                    
            if self.__mode == "linear":
                self.__error.configure(text = "")
                try:
                    x = float(self.__one_entry.get())
                    number = float(self.__number_entry.get())
                    answer = float(self.__answer_entry.get())
                    self.root1 = (answer - number) / x 
                    self.__answer_x1.configure(text= f"X1 = {self.root1}")
                    if self.var.get():
                        self.round_result()
                except ZeroDivisionError:
                    self.__error.configure(text = "Error: ne mojet bit ravno nulu")
                    
        except ValueError:
            self.__error.configure(text = "Error: nevernoe znach")
    
    def reset_fields(self):
        
        self.__quadratic_entry.delete(0, END)
        self.__cub_entry.delete(0, END)
        self.__one_entry.delete(0, END)
        self.__number_entry.delete(0, END)
        self.__answer_entry.delete(0, END)
        self.__error.configure(text = "")
        if self.__mode == "cubic":
            self.__answer_x1.configure(text= "X1 = ")
            self.__answer_x2.configure(text= "X2 = ")
            self.__answer_x3.configure(text= "X3 = ")
        if self.__mode == "square":
            self.__answer_x1.configure(text= "X1 = ")
            self.__answer_x2.configure(text= "X2 = ")
        if self.__mode == "linear":
            self.__answer_x1.configure(text= "X1 = ")
           
    def round_result(self):
        if self.var.get():
            try:
                if self.__mode == "cubic":
                    self.__answer_x1["text"] = 'X1 = {:.{}f}'.format( self.root1, 2 )
                    self.__answer_x2["text"] = 'X2 = {:.{}f}'.format( self.root2, 2 )
                    self.__answer_x3["text"] = 'X3 = {:.{}f}'.format( self.root3, 2 )
                if self.__mode == "square":
                    self.__answer_x1["text"] = 'X1 = {:.{}f}'.format( self.root1, 2 )
                    self.__answer_x2["text"] = 'X2 = {:.{}f}'.format( self.root2, 2 )
                if self.__mode == "linear":
                    self.__answer_x1["text"] = 'X1 = {:.{}f}'.format( self.root1, 2 )
            except AttributeError:
                self.root1 = 0
                
    def two_system(self):
        self.__cub_entry.grid_remove()
        self.__quadratic_entry.grid_remove()
        self.__one_entry.grid_remove()
        self.__number_entry.grid_remove()
        self.__answer_entry.grid_remove()
        self.__cub_text.grid_remove()
        self.__quadratic_text.grid_remove()
        self.__one_x_text.grid_remove()
        self.__equally_text.grid_remove()
        self.__answer_x1.grid_remove()
        self.__answer_x2.grid_remove()
        self.__answer_x3.grid_remove()
        self.cb.grid_remove()
    
    def tree_system(self):
        self.__cub_entry.grid_remove()
        self.__quadratic_entry.grid_remove()
        self.__one_entry.grid_remove()
        self.__number_entry.grid_remove()
        self.__answer_entry.grid_remove()
        self.__cub_text.grid_remove()
        self.__quadratic_text.grid_remove()
        self.__one_x_text.grid_remove()
        self.__equally_text.grid_remove()
        self.__answer_x1.grid_remove()
        self.__answer_x2.grid_remove()
        self.__answer_x3.grid_remove()
        self.cb.grid_remove()
    
def main():
    
    ui = Userinterface()



if __name__ == "__main__":
    main()
