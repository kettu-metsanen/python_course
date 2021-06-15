"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def main():
    chos = int(input("Choose a number: "))
    i = 1
    while i <=10:
        print(i, "*", chos, "=", i*chos)
        i += 1
        
if __name__ == "__main__":
    main()  