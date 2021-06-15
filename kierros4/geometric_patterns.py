"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
""" 
from math import pi

def circumference_kvadrat(a):
    """laske ympärysmitta neliö"""
    per_kvadr = a * 4
    return per_kvadr
def circumference_pramug(a,b):
    """laske ympärysmitta suorakaide"""
    per_pramug = 2 * (a + b)
    return per_pramug
def circumference_krug(r):
    """laske ympärysmitta ympyrä"""
    per_krug = 2 * pi * r
    return per_krug
def area_kvadrat(a):
    """laske pinta-ala neliö"""
    pl_kv = a * a
    return pl_kv
def area_pramug(a,b):
    """laske pinta-ala suorakaide"""
    pl_pr = a * b
    return pl_pr
def area_krug(r):
    """laske pinta-ala ympyrä"""
    pl_kr = pi * r * r
    return pl_kr
def tarkastus(k):
    """tarkista että luku isompi kuin nolla"""
    if k > 0:
        return 1
    else:
        return 0
def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            i = 0
            while i == 0:
                st_kv = float(input("Enter the length of the square's side: "))
                i = tarkastus(st_kv)
            vast_cir = circumference_kvadrat(st_kv)
            vast_area = area_kvadrat(st_kv)
            print(f"The circumference is {vast_cir:.2f}")
            print(f"The surface area is {vast_area:.2f}")
            pass

        elif answer == "r":
            i = 0
            while i == 0:
                st_pr1 = float(input("Enter the length of the rectangle's side 1: "))
                i = tarkastus(st_pr1)
            j = 0
            while j == 0:
                st_pr2 = float(input("Enter the length of the rectangle's side 2: "))
                j = tarkastus(st_pr2)
            vast_cir = circumference_pramug(st_pr1, st_pr2)
            vast_area = area_pramug(st_pr1, st_pr2)
            print(f"The circumference is {vast_cir:.2f}")
            print(f"The surface area is {vast_area:.2f}")
            pass
        
        elif answer == "c":
            i = 0
            while i == 0:
                st_kr = float(input("Enter the circle's radius: "))
                i = tarkastus(st_kr)
            vast_cir = circumference_krug(st_kr)
            vast_area = area_krug(st_kr)
            print(f"The circumference is {vast_cir:.2f}")
            print(f"The surface area is {vast_area:.2f}")
            pass

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()

def main():
    menu()
    print("Goodbye!")

if __name__ == "__main__":
    main()
