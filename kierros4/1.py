"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
EPSILON = 0.000000001
def compare_floats(luku1, luku2, EPSILON):
    """ottaa parametrinaan kaksi liukulukua sekä vertailussa 
    käytettävän epsilonin arvon ja palauttaa totuusarvona tiedon"""
    if abs(luku1-luku2) <EPSILON:
        return True
    else:
        return False
def main():
    chislo1 = float(input("Luku a: "))
    chislo2 = float(input("Luku b: "))
    print(compare_floats(chislo1, chislo2,EPSILON ))

if __name__ == "__main__":
  main()
