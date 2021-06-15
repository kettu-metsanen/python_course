"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""


def read_file(filename):
    """ Tässä avataan tiedosto, luetaan jokainen rivi,
        luodaan sanakirja ja täyttetään se
    
    parametri:
    filename: tiedoston nimi
    return: 
    subjects: sanakirja, missa on info tiedostosta
    None: tämä palauttetaan jos on virhe
    """
    subjects  = {}
    try:
        with open(filename, 'r') as file:
            contents = file.readlines()
        for row in contents: # täyttetään sanakirja
            row = row.strip()
            dept, name, ects = row.split(";")
            if dept not in subjects.keys():
                subjects[dept] = {}
                subjects[dept][name] = ects
            else:
                subjects[dept][name] = ects
        return subjects
    except IOError:
        print("Error opening file!")
        return None
    except ValueError:
        print("Error in file!")
        return None
  
def add_in_dict(mass, comentot):
    """ Lisataan sanakirjaan uusi info
    
    parametri:
    mass: aiemmin luotu sanakirja
    comentot: rivi komennon kanssa
    return: 
    mass: päivitetty sanakirja
    """
    if len(comentot) < 3: # Tarkistetaan että komennossa on osasto ja kirssi
        print("Invalid command!")
        return mass
    else:
        department = comentot[1]
        op = comentot[-1]
        cours = comentot[2:-1]
        cours_all = ""
        if department in mass: # lisataan kurssit
            for i in range(len(cours)):
                if cours[i] == cours[-1]:
                    cours_all += cours[i]
                else:
                    cours_all += cours[i] + " "
            mass[department][cours_all] = op
            print(f"Added course {cours_all} to department {department}")
            return mass
        else: # lisataan osasto
            mass[department] = {}
            for i in range(len(cours)):
                if cours[i] == cours[-1]:
                    cours_all += cours[i]
                else:
                    cours_all += cours[i] + " "
            mass[department][cours_all] = op
            print(f"Added department {department} with course {cours_all}")
            return mass
        
def print_all(mass):
    """ Tulostetaan kaikki info tiedostosta tietyssä muodossa
    
    parametri:
    mass: aiemmin luotu sanakirja
    
    """
    for name in sorted(mass.keys()):
        print("*", name, "*", sep="")
        for cours in sorted(mass[name].keys()):
            arvo = mass[name][cours]
            print(cours, ":", arvo, "cr")
    return 0

def print_dep(mass, arvo):
    """ Tulostetaan tietty osasto
    
    parametri:
    mass: aiemmin luotu sanakirja
    arvo: rivi komennon kanssa
    
    """
    name = arvo[1]
    if name in mass:
        print("*", name, "*", sep="")
        for cours in sorted(mass[name].keys()):
            arvo = mass[name][cours]
            print(cours, ":", arvo, "cr")
    if name not in mass:
        print("Department not found!")
    return 0

def print_credits(mass, arvo):
    """ Tulostetaan tietyn osaston opintopisteet
    
    parametri:
    mass: aiemmin luotu sanakirja
    arvo: rivi komennon kanssa
    
    """
    name = arvo[1]
    summ = 0
    if name in mass:
        for cours in sorted(mass[name].keys()):
            arvo = mass[name][cours]
            summ += int(arvo)
        print()            
        print(f"Department {name} has to offer {summ} cr.")
    if name not in mass:
        print("Department not found!")

def delite_part(mass, comentot):
    """ Poistetaan sanakirjasta tietyt osastot tai kurssit
    
    parametri:
    mass: aiemmin luotu sanakirja
    comentot: rivi komennon kanssa
    return: 
    mass: päivitetty sanakirja
    """
    if len(comentot) == 2: # poistetaan osasto
        depart = comentot[1]
        if depart not in mass:
            print(f"Department {comentot[1]} not found!")
        else:
            del mass[depart]
            print(f"Department {comentot[1]} removed.")
            return mass
    else: # poistetaan kurssi
        department = comentot[1]
        cours = comentot[2:]
        cours_all = ""
        for i in range(len(cours)):
            if cours[i] == cours[-1]:
                cours_all += cours[i]
            else:
                cours_all += cours[i] + " "
        if cours_all in mass[department]:
            del mass[department][cours_all]
            print(f"Department {department} course {cours_all} removed.")
            return mass
        else:
            print(f"Course {cours_all} from {department} not found!")
def main():
    
     filename = input("Enter file name: ")
     data = read_file(filename)
     if data != None:
         print()
         print("[A]dd / [C]redits / [D]elete / [P]rint all / p[R]int department / [Q]uit")
         comento = input("Enter command: ")
         comento_split = comento.split()
         while True:
            if comento_split[0] == "a" or comento_split[0] == "A":
                print()
                data = add_in_dict(data, comento_split)
            elif comento_split[0] == "c" or comento_split[0] == "C":
                print_credits(data, comento_split)
            elif comento_split[0] == "d" or comento_split[0] == "D":
                delite_part(data, comento_split)
            elif comento_split[0] == "p" or comento_split[0] == "P":
                print()
                print_all(data)
            elif comento_split[0] == "r" or comento_split[0] == "R":
                print()
                print_dep(data, comento_split)
            elif comento_split[0] == "q" or comento_split[0] == "Q":
                print("Ending program.")
                break
            else:
                print("Invalid command!")
            print()
            print("[A]dd / [C]redits / [D]elete / [P]rint all / p[R]int department / [Q]uit")
            comento = input("Enter command: ")
            comento_split = comento.split()
if __name__ == "__main__":
    main()  

    
