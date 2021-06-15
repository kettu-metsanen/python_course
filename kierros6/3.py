"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def create_an_acronym(text):
    """
    Akronyymin muodostaminen

    Parameters
    ----------
    text : sanat

    Returns
    -------
    Vastaus summ

    """
    delim_text = text.split()
    summ = ""
    for i in range(0, len(delim_text)):
        slovo = delim_text[i]
        slovo_new = slovo.upper()
        summ += slovo_new[0]
    return summ
def main():
   
    txt = input("Vvedi text: ")
    print(create_an_acronym(txt))
           
   
if __name__ == "__main__":
  main()