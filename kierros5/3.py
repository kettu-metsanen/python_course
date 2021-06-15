"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""

def main():
    
    lukut_mita_haluat = []
    print("Give 5 numbers:")
    i = 1
    while i <=5:
        lukut_mita_haluat.append(input("Next number: "))
        i += 1
    print("The numbers you entered, in reverse order:")
    for k in range(4, -1, -1):
        print(lukut_mita_haluat[k])
   
if __name__ == "__main__":
  main()