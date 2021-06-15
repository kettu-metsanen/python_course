"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def read_message():
    """
    Razdelaem text na list

    Parameters
    ----------
    text : TYPE
        DESCRIPTION.

    Returns
    -------
    new_list : TYPE
        DESCRIPTION.

    """
    our_list = []
    inp = input()
    our_list.append(inp)
    while inp != "":
        inp = input()
        our_list.append(inp)
    our_list.remove("")
    return our_list


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    
    msg = read_message()
    
    print("The same, shouting:")
   
    for i in range(0, len(msg)):
        sano = msg[i]
        new_sano = sano.upper()
        print(new_sano)
       

if __name__ == "__main__":
    main()
