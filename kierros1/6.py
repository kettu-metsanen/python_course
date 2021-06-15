"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def main():
    
    pl1 = input("Player 1, enter your choice (R/P/S): ")
    pl2 = input("Player 2, enter your choice (R/P/S): ")
    if pl1 == pl2:
        print("It's a tie!")
    elif pl1 == "R":
        if pl2 == "S":
            print("Player 1 won!")
        else:
            print("Player 2 won!")
    elif pl1 == "P":
        if pl2 == "R":
            print("Player 1 won!")
        else:
            print("Player 2 won!")
    elif pl1 == "S":
        if pl2 == "P":
            print("Player 1 won!")
        else:
            print("Player 2 won!")
    
if __name__ == "__main__":
    main()
    