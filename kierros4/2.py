"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
import math 
def tarkista(yht, on):
    """tarkista onko mollemmat positivinen ja onko lottopallojen kokonaismäärä
    isompi entä arvottavien pallojen määrän"""
    if on > yht or on < 0 or yht < 0:
        return False
    else:
        return True
    
def podschet(yht, on):
    """lsku faktorial ja antaa vastaus"""
    if tarkista(yht, on) == True:
        fact = (math.factorial(yht)) / (math.factorial(yht - on) * math.factorial(on))
        return fact
    elif tarkista(yht, on) == False:
        return 0
    

def main():
    
    vsego = int(input("Enter the total number of lottery balls: "))
    nujno = int(input("Enter the number of the drawn balls: "))
    
    vast = podschet(vsego, nujno)
    if vast == 0:
        if nujno < 0 or vsego < 0:
            print("The number of balls must be a positive number.")
        elif nujno > vsego:
            print("At most the total number of balls can be drawn.")
    elif vast > 0:
        print(f"The probability of guessing all {nujno} balls correctly is 1/{vast:.0f}")

if __name__ == "__main__":
  main()