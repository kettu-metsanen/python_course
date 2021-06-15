"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""

def read_input(nimi):
    """Tarkista onko luku isompi 0"""
    luku = int(input(nimi))
    while luku < 1:
        luku = int(input(nimi))
    return luku
def print_box(width, height, border_mark = "#", inner_mark = " "):
    """ohjelma tulostaa hienoja ruutuja"""
    i = 1
    j = 1
    while i <=  height:
        if i == 1 or i == height:
            while j <= width:
                if j == width:
                    print(border_mark)
                else:
                    print(border_mark, end="")
                j += 1
        else:
            while j <= width:
                if j == width:
                    print(border_mark)
                elif j == 1:
                    print(border_mark, end="")
                else:
                    print(inner_mark, end="")
                j += 1
        j = 1
        i += 1

def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


# TODO: the definition of print_box could also go here, it is up to you.


if __name__ == "__main__":
    main()
