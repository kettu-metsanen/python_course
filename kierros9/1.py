"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def read_file(nimi):
    baza = {}
    with open(nimi, 'r') as file:
        contents = file.readlines()
    ks = contents[0].strip().split(';')
    baza = dict.fromkeys(ks)
    contents = contents[1:]
    for names in contents:
        data = names.split(';')
        for i in data[:-1]:
           for j in baza:
               baza[j].append(i)
    return baza

    

def main():
    #filename = input("Enter the name of the file: ")
    filename = 'contacts.csv'
    baza_znach = read_file(filename)
    print(baza_znach)
if __name__ == "__main__":
    main()  
    #contacts.csv
    
