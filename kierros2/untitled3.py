"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def main():
    chos = int(input("Choose a number: "))
    i = 1
    k = 0
    while k < 100:
        print(i, "*", chos, "=", i*chos)
        i += 1
        k = i * chos
    print(i, "*", chos, "=", i*chos)
if __name__ == "__main__":
    main()  