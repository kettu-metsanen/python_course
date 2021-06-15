"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def main():
    i = 1
    f1 = 1
    f2=1
    skolko = int(input("How many Fibonacci numbers do you want? "))
    while i<= skolko: 
        res = f1 + f2
        if i ==1:
            print(i, ". ", f1, sep="")
        elif i == 2:
            print(i, ". ", f2, sep="")
        elif i == 3:
            print(i, ". ", res, sep="")
            f1=res
        else:
            print(i, ". ", res, sep="")
            f2 = f1
            f1 = res
            
        
        i += 1
if __name__ == "__main__":
    main()
    