"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def main():
    
    luku = int(input("How many numbers would you like to have? "))
    for vivod in range(1,luku+1):
        if (vivod%3 == 0 and vivod%7 == 0):
            print("zip boing")
        elif vivod%7 == 0:
            print("boing")
        elif vivod%3 == 0:
            print("zip")
        else:
            print(vivod)
    
if __name__ == "__main__":
    main()  