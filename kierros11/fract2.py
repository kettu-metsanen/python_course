"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""

class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """
    
    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.
        
        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """
        
        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError
        
        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError
        
        self.__numerator = numerator
        self.__denominator = denominator
    
    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
           numerator/denominator.
        """
        
        if self.__numerator * self.__denominator < 0:
            sign = "-"
        
        else:
            sign = ""
        
        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"
        
    def simplify(self):
        """
        :returns: str, a string-presentation of the fraction in the format
           numerator/denominator.
        """
        obsh = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator//obsh
        self.__denominator = self.__denominator//obsh

    def complement(self):
        
        
        result_ob = Fraction(self.__numerator*(-1), self.__denominator)   
        return result_ob
    def reciprocal(self):
        
        result_ob = Fraction(self.__denominator, self.__numerator) 
        return result_ob
        
    def multiply(self, frac2):
        verh = self.__numerator * frac2.__numerator 
        biz = self.__denominator * frac2.__denominator
        
        result_ob = Fraction(verh, biz)
        return result_ob
        
    def divide(self, frac2):
        
        verh = self.__numerator * frac2.__denominator
        biz = self.__denominator * frac2.__numerator
        result_ob = Fraction(verh, biz)
        return result_ob
        
    def add(self, frac2):
        
        vverh = (self.__numerator * frac2.__denominator) + (self.__denominator * frac2.__numerator)
        niz = self.__denominator * frac2.__denominator
        result_ob = Fraction(vverh, niz)
        return result_ob
    def deduct(self, frac2):
       
       vverh = (self.__numerator * frac2.__denominator) - (self.__denominator * frac2.__numerator)
       niz = self.__denominator * frac2.__denominator
       result_ob = Fraction(vverh, niz)
       return result_ob
        
    def __lt__(self, frac2):
       
        if self.__numerator * frac2.__denominator < frac2.__numerator * self.__denominator:
            return True
        else: 
            return False
          
    def __le__(self, frac2):
        
        if self.__numerator * frac2.__denominator > frac2.__numerator * self.__denominator:
            return True
        else: 
            return False
        
    def __str__(self):
        
        if self.__numerator * self.__denominator < 0:
            sign = "-"
        
        else:
            sign = ""
        
        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"
        
def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a
def read_file(filename):
    """ Tässä avataan tiedosto, luetaan jokainen rivi,
        luodaan sanakirja ja täyttetään se
    
    parametri:
    filename: tiedoston nimi
    return: 
    subjects: sanakirja, missa on info tiedostosta
    None: tämä palauttetaan jos on virhe
    """
    subjects  = {}
    try:
        with open(filename, 'r') as file:
            contents = file.readlines()
        for row in contents: # täyttetään sanakirja
            row = row.strip()
            name, drob = row.split("=")
            spl_test = drob.split("/")
            a = Fraction(int(spl_test[0]), int(spl_test[1]))
            subjects[name] = a
        return subjects
    except IOError:
        print("Error: the file cannot be read.")
        return None
    except ValueError:
        print("Error in file!")
        return None
    except IndexError:
        print("Error: the file cannot be read.")
def main():
    sanakir = {}
    comant = input("> ")
    while comant != "quit":
        if comant == "add":
            test=input("Enter a fraction in the form integer/integer: ")
            spl_test = test.split("/")
            a = Fraction(int(spl_test[0]), int(spl_test[1]))
            b=input("Enter a name: ")
            sanakir[b] = a
        elif comant == "print":
            nimi = input("Enter a name: ")
            if nimi in sanakir:
                vast = sanakir[nimi]
                print(nimi,"=", vast)
            else:
                print(f"Name {nimi} was not found")
        elif comant == "list":
            for i in sorted(sanakir):
                print(i, "=", sanakir[i])
        elif comant == "*":
            nimi1 = input("1st operand: ")
            if nimi1 in sanakir: 
                nimi2 = input("2nd operand: ")
                if nimi2 not in sanakir:
                    print(f"Name {nimi2} was not found")
                else:
                    dr1 = sanakir[nimi1]
                    dr2 = sanakir[nimi2]
                    umn = dr1.multiply(dr2)
                    print(sanakir[nimi1], "*", sanakir[nimi2], "=", umn)
                    umn.simplify()
                    print("simplified", umn)
            else:
                nimi1 not in sanakir
                print(f"Name {nimi1} was not found")
                
        elif comant == "file":
            nime_fail = input("Enter the name of the file: ")
            new_sanakir = read_file(nime_fail)
            if new_sanakir != None:
                for j in new_sanakir:
                    sanakir[j] = new_sanakir[j]
        else:
            print("Unknown command!")
        comant = input("> ")
    print("Bye bye!")
if __name__ == "__main__":
    main()