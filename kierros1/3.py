"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
index = 1.17
znach = input("Enter the amount of the study benefits: ")
raha = float(znach)
ensind = raha * (index/100) + raha
print("If the index raise is", index, "percent, the study benefit,")
print("after a raise, would be", ensind, "euros")
toinind = ensind * (index/100) + ensind
print("and if there was another index raise, the study")
print("benefits would be as much as", toinind, "euros")
