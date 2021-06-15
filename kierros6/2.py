"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def reverse_name(text):
    """
    Käännä nimet oikein päin

    Parameters
    ----------
    text : Nimi ja Sukunmi

    Returns
    -------
    Vastaus

    """
    zapataja = "," in text
    if zapataja == 1:
        razdeleno = text.split(",")
        if razdeleno[0] == "" or razdeleno[1] == "" or razdeleno[0] == " " or razdeleno[1] == " ":
            vivod = razdeleno[1].strip() + razdeleno[0].strip()
        else:
            vivod = razdeleno[1].strip() + " " + razdeleno[0].strip()
        return vivod
    else:
        razdeleno = text.split()
        if len(razdeleno) == 1:
            vivod = razdeleno[0]
            
        else:
            vivod = razdeleno[0] + " " + razdeleno[1]
            
        return vivod.strip("")
    
    
def main():
   
    txt = input("Vvedi ima: ")
    print(reverse_name(txt))
           
   
if __name__ == "__main__":
  main()