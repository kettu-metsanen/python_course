"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""

def longest_substring_in_order(text): 
    """
    Pisin järjestetty alimerkkijono

    Parameters
    ----------
    text : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if len(text) == 0 or len(text) == 1:
        return text
    jonot = []
    for i in range(len(text)):
        cursym = text[i]
        jono = cursym
        for j in range(i+1, len(text)):
            if j == len(text)-1:
                if text[j] > text[j-1]:
                    jono += text[j]
                    jonot.append(jono)
            elif text[j] > cursym:
                jono += text[j]
                cursym = text[j]
            else:
                #print(jono)
                jonot.append(jono)
                jono = ""
                break
                #i = j-1
    return (max(jonot, key=len))


def main():
    txt = input("Vvedi text: ")
    print(longest_substring_in_order(txt))
   
    
   
if __name__ == "__main__":
  main()