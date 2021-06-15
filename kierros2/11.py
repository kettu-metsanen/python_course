"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def main():
    answer = input("Bored? (y/n) ")
    while (answer != "y" and answer != "Y"):
        if not answer == "n" or answer == "N":
            print("Incorrect entry.")
        answer = input("Bored? (y/n) ")        
    print("Well, let's stop this, then.")
    
if __name__ == "__main__":
    main()