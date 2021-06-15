"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def input_to_list(chislo):
    """ input lukut kun tiedan paljonko lukut halutaan"""
    luku_mita_haluat = []
    print(f"Enter {chislo} numbers:")
    i = 1
    while i <= chislo:
        luku_mita_haluat.append(int(input()))
        i += 1
    return luku_mita_haluat
def main():

    nujnoe_chislo = int(input("How many numbers do you want to process: "))
    massiv = input_to_list(nujnoe_chislo)
    ishem = int(input("Enter the number to be searched: "))
    i = 0
    summ = 0
    while i < int(nujnoe_chislo) :
        if ishem == massiv[i]:
            summ += 1
        i += 1
    if summ > 0:
        print(f"{ishem} shows up {summ} times among the numbers you have entered.")
    else:
        print(f"{ishem} is not among the numbers you have entered.")
    
if __name__ == "__main__":
  main()