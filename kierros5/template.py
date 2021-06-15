"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
# TODO: add the definition for convert_grades here
def convert_grades(mass):
    """Vaihta kaikki lukut isompi 0 kuudessa"""
    for i in range(0,len(mass)):
        if mass[i] != 0:
            mass[i] = 6

def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
