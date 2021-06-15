"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
    
def capitalize_initial_letters(text):
    """
    Isot alkukirjaimet paikoilleen

    Parameters
    ----------
    text : sanat

    Returns
    -------
    Vastaus 

    """
    return text.title()

def main():
   
    txt = input("Vvedi text: ")
    print(capitalize_initial_letters(txt))
           
   
if __name__ == "__main__":
  main()