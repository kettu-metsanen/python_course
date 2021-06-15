"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def main():
    answer = input("Answer Y or N: ")
    while (answer != "n" and answer != "N") and (answer != "y" and answer != "Y"):
        print("Incorrect entry.")
        answer = input("Answer Y or N: ")    
    print("You answered", answer)
    
if __name__ == "__main__":
    main()