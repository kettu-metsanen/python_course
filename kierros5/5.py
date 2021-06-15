"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def  are_all_members_same(mass):
    """ löydä min ja max ja tarkista onko se sama"""
    if mass == []:
        return True
    elif max(mass) == min(mass):
        return True
    else: 
        return False
    
def main():
    mass1 = [42, 42, 42, 43, 42]
    mass2 = [42, 42, 42, 42, 42]
    mass3 = []
    print("Jos [42, 42, 42, 43, 42]", are_all_members_same(mass1))
    print("Jos [42, 42, 42, 42, 42]", are_all_members_same(mass2))
    print("Jos []", are_all_members_same(mass3))
    
if __name__ == "__main__":
  main()