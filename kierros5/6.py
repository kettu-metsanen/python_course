"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def  is_the_list_in_order(mass):
    """ sort ja tarkista onko se sama"""
    if mass == []:
        return True
    elif sorted(mass) == mass:
        return True
    else: 
        return False
    
def main():
    mass1 = [37, 42, 43]
    mass2 = [42, 37, 43]
    mass3 = []
    mass4 = [1]
    print("Jos [37, 42, 43]", is_the_list_in_order(mass1))
    print("Jos [42, 37, 43]", is_the_list_in_order(mass2))
    print("Jos []", is_the_list_in_order(mass3))
    print("Jos [1]", is_the_list_in_order(mass4))
if __name__ == "__main__":
  main()