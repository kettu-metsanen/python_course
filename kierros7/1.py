"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def main():
    print("Enter rows of text for word counting. Empty row to quit.")
    znach = input()
    sanakirja = dict()
    while znach != "":
        new_list = znach.split()
        for i in new_list:
            i = i.lower()
            if i in sanakirja:
                k = sanakirja[i]
                sanakirja[i] = k + 1
            else:
                sanakirja[i] = 1
        znach = input()
    for word in sorted(sanakirja):
        print(word, ":", sanakirja[word], "times")

if __name__ == "__main__":
    main()  
"""    
I'm on a high way to hell
I'm on a high way to hell
It's going really well
Well it's only hell
"""