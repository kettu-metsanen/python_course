"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def main():
    sum = 0
    i = 1
    j = 1
    x = 1
    luku = int(input("Enter the number of months: "))
    while x <= luku:
        if i == 0 and j == 0:
            break
        pistet=int(input(f"Enter the number of credits in month {x}: "))
        sum += pistet
        j = i
        i = pistet
        x += 1
    if i == 0 and j == 0:
        print()
        print("You did have too many study breaks!")
    elif sum/luku < 5:
        print()
        print(f"Your monthly credit point average {sum/luku:.1f} does not classify you as a full time student.")
    else:
        print()
        print(f"You are a full time student and your monthly credit point average is {sum/luku:.1f}.")
if __name__ == "__main__":
    main()