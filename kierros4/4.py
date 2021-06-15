"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""

def calculate_angle(A, B = 90):
    """lasku kolmion kulma. Tiedan etta kaiki kulmat kolmiossa on 180"""
    C = 180 - A - B
    return C

def main():
    lineA = int(input("Ensimainen kulma: "))
    lineB = int(input("Toinen kulma: "))
    
    kulma = calculate_angle(lineA, lineB)
    print(f"The triangle's area is {kulma:.0f}")


if __name__ == "__main__":
    main()