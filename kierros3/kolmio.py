"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
from math import sqrt
def area(sideA,sideB,sideC):
    """lasku kolmion pintaala"""
    s = (sideA + sideB + sideC)/2
    A = sqrt(s*(s-sideA)*(s-sideB)*(s-sideC))
    return A

def main():
    lineA = float(input("Enter the length of the first side: "))
    lineB = float(input("Enter the length of the second side: "))
    lineC = float(input("Enter the length of the third side: "))
    area_lasku = area(lineA, lineB, lineC)
    print(f"The triangle's area is {area_lasku:.1f}")


if __name__ == "__main__":
    main()
