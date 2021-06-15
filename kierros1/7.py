"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def main():
    
    cost = input("Purchase price: ")
    price = int(cost)
    raha = input("Paid amount of money: ")
    money = int(raha)
    summa = int(money - price)
    summa10 = summa - summa//10*10
    summs5 = (summa10)//5
    summa2 = (summa10-summs5*5)//2
    if money == price or money < price:
        print("No change")
    elif summa//10 > 0:
        print("Offer change:")
        print(summa//10, "ten-euro notes")
        if summs5 > 0:
            print(summs5, "five-euro notes")
            if (summa10-summs5*5)//2 > 0:
                print((summa10-summs5*5)//2, "two-euro coins")
                if (summa10-summs5*5 - summa2 * 2) > 0:
                    print((summa10-summs5*5 - summa2 * 2), "one-euro coins")
            else:
                print((summa10)//5, "one-euro coins")
        elif (summa10)//2 > 0:
                print((summa10)//2, "two-euro coins")
                if (summa10-(summa10//2*2)) > 0:
                    print((summa10-(summa10//2*2)), "one-euro coins")
        elif summa10 > 0:
                print(summa10, "one-euro coins")
    elif summs5 > 0:
        print("Offer change:")
        print(summs5, "five-euro notes")
        if (summa10-summs5*5)//2 > 0:
            print((summa10-summs5*5)//2, "two-euro coins")
            if (summa10-summs5*5 - summa2 * 2) > 0:
                print((summa10-summs5*5 - summa2 * 2), "one-euro coins")
        elif (summa10)-(summa10)//5*5 > 0:
            print((summa10)-(summa10)//5*5, "one-euro coins")
    elif (summa10)//2 > 0:
        print("Offer change:")
        print((summa10)//2, "two-euro coins")
        if (summa10-(summa10//2*2)) > 0:
            print((summa10-(summa10//2*2)), "one-euro coins")
    elif summa10 > 0:
        print("Offer change:")
        print(summa10, "one-euro coins")
    
if __name__ == "__main__":
    main()
    