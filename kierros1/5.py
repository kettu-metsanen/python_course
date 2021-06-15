"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def main():
    
    znach = input("How do you feel? (1-10) ")
    nastr = int(znach)
    if nastr >= 1 and nastr <= 10:
        if nastr == 1:
            print("A suitable smiley would be :'(")
        elif nastr >=2 and nastr <=3:
            print("A suitable smiley would be :-(")
        elif nastr >=4 and nastr <=7:
            print("A suitable smiley would be :-|")
        elif nastr >=8 and nastr <=9:
            print("A suitable smiley would be :-)")
        elif nastr == 10:
            print("A suitable smiley would be :-D")
    else:
        print("Bad input!")
if __name__ == "__main__":
    main()
    