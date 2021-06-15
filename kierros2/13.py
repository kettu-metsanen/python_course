"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def main():
    k = 1
    for i in range(3,32,7):
        print(i,".",k,".", sep="")
    for i in range(7,29,7):
        print(i,".",k+1,".", sep="")
    for i in range(7,32,7):
        print(i,".",k+2,".", sep="")
    for i in range(4,31,7):
        print(i,".",k+3,".", sep="")
    for i in range(2,32,7):
        print(i,".",k+4,".", sep="")
    for i in range(6,31,7):
        print(i,".",k+5,".", sep="")
    for i in range(4,32,7):
        print(i,".",k+6,".", sep="")
    for i in range(1,32,7):
        print(i,".",k+7,".", sep="")
    for i in range(5,31,7):
        print(i,".",k+8,".", sep="")
    for i in range(3,32,7):
        print(i,".",k+9,".", sep="")
    for i in range(7,31,7):
        print(i,".",k+10,".", sep="")
    for i in range(5,32,7):
        print(i,".",k+11,".", sep="")
    
    
if __name__ == "__main__":
    main()