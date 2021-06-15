"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
    
def count_abbas(text):
    """
    Isot alkukirjaimet paikoilleen

    Parameters
    ----------
    text : sanat

    Returns
    -------
    Vastaus 

    """
    summ = 0
    for i in range(0, len(text)-3):
        if text[i] == "a" and text[i+3] == "a":
            if text[i+1] == "b" and text[i+2] == "b":
                summ +=1
    return summ

def main():
   
    txt = input("Vvedi text: ")
    print(count_abbas(txt))
           
   
if __name__ == "__main__":
  main()