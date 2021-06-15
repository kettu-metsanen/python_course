"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def print_verse(sanoY, sanoK):
    """ tulostaa laulun Old MacDonald Had a Farm sanoituksen"""
    if sanoY == "lamb":
        print("Old MACDONALD had a farm")
        print("E-I-E-I-O")
        print("And on his farm he had a", sanoY)
        print("E-I-E-I-O")
        print("With a", sanoK, sanoK, "here")
        print("And a", sanoK, sanoK, "there")
        print("Here a ", sanoK,", there a ", sanoK, sep=(""))
        print("Everywhere a", sanoK, sanoK)
        print("Old MacDonald had a farm")
        print("E-I-E-I-O")
    else:
        print("Old MACDONALD had a farm")
        print("E-I-E-I-O")
        print("And on his farm he had a", sanoY)
        print("E-I-E-I-O")
        print("With a", sanoK, sanoK, "here")
        print("And a", sanoK, sanoK, "there")
        print("Here a ", sanoK,", there a ", sanoK, sep=(""))
        print("Everywhere a", sanoK, sanoK)
        print("Old MacDonald had a farm")
        print("E-I-E-I-O")
        print()
def main():
    print_verse("cow", "moo")
    print_verse("pig", "oink")
    print_verse("duck", "quack")
    print_verse("horse", "neigh")
    print_verse("lamb", "baa")

if __name__ == "__main__":
    main()
