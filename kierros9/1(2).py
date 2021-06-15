"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""

def read_file(filename):
    """
    

    Parameters
    ----------
    filename : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    abook = {}
    with open(filename, 'r') as file:
        contents = file.readlines()
#print(contents)
    for st in contents[1:]:
        temp = {}
        tlist = st.split(';')
        temp['name'] = tlist[1].strip()
        temp['phone'] = tlist[2].strip()
        temp['email'] = tlist[3].strip()
        temp['skype'] = tlist[4].strip()
        abook[tlist[0]] = temp
    #print(abook)
    return abook

def main():
    filename = input("Enter the name of the file: ")
    info = read_file(filename)
    #breakpoint()

if __name__ == "__main__":
    main()