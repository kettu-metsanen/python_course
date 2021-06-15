"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def repeat_name(nimi, luku):
    """Funktiolle välitetään ensimmäisenä parametrina karhun etunimi 
    ja toisena parametrina toistojen lukumäärä"""
    i = 1
    while i <= luku:
        print(nimi,", ", nimi, " Bear", sep=(""))
        i+=1

def verse(lause, name):
    """ laulun sanat tulostava"""
    if name == "Cindy":
        print(lause)
        print(name, ", ", name, sep=(""))
        print(lause)
        repeat_name(name, 3)
        
        print(lause)
        repeat_name(name, 1)
    else:
        print(lause)
        print(name, ", ", name, sep=(""))
        print(lause)
        repeat_name(name, 3)
        print(lause)
        repeat_name(name, 1)
        print()
def main():
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")
    

if __name__ == "__main__":
    main()
