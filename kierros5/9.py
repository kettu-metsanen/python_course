"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def sravnenie(mass, vrema):
    """ Tarkista mita aika nym ja koska seurava bussi"""
    for i in range(0,len(mass)):
        if vrema <= int(mass[i]):
            start_znach = i
            break
        else:
            start_znach = 0
    return start_znach
def main():
   
    aikataulu = [630, 1015, 1415, 1620, 1720, 2000]
    vrema_seichas = int(input("Enter the time (as an integer): "))
    print("The next buses leave:")
    znach = sravnenie(aikataulu, vrema_seichas)
    for i in range(1, 4):
        if i == 1:
            print(aikataulu[znach])
            i += 1
            znach += 1
        else:
            if znach >= len(aikataulu):
                znach = 0
            print(aikataulu[znach])
            znach += 1
    
if __name__ == "__main__":
  main()