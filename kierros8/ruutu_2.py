"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def read_input(nimi):
    """Tarkista onko luku isompi 0"""
    znach = True
    while znach:
        
        try:
            luku = int(input(nimi))
            while luku < 1:
                luku = int(input(nimi))
            return luku
            znach = False
        except ValueError:
            continue
def print_box(width, height, mark):
    """ohjelma tulostaa hienoja ruutuja"""
    i = 1
    j = 1
    while i <=  height:
        while j <= width:
            if j == width:
                print(mark)
            else:
                print(mark, end="")
            j += 1
        j = 1
        i += 1
        
def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
