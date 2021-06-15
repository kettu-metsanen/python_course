"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
  
def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    if text.istitle() == 1:
        new_text = text.lower()        
        if new_text in regular_chars:
            index_znach = regular_chars.index(new_text)
            rezult = encrypted_chars[index_znach].upper()
            
        else:
            rezult = text
    else:       
        if text in regular_chars:
            index_znach = regular_chars.index(text)
            rezult = encrypted_chars[index_znach]
            
        else:
            rezult = text
    return rezult
def row_encryption(text):
    """
    Vizivaem funkciyu kotoraja preobrazovivaet bukvi v kod

    Parameters
    ----------
    text : TYPE
        DESCRIPTION.

    Returns
    -------
    summ : TYPE
        DESCRIPTION.

    """
    summ = ""
    for i in range(0, len(text)):
        summ+= encrypt(text[i])
    return summ
def main():
   
    txt = input("Vvedi text: ")
    print(row_encryption(txt))
           
   
if __name__ == "__main__":
  main()