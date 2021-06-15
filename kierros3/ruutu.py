"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
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
    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
