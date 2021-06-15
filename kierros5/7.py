"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""

def main():
   mass = []
   for i in range(1,6):
       mass.append(float(input(f"Enter the time for performance {i}: ")))

   mass.remove(max(mass))
   mass.remove(min(mass))
   summ = 0
   for k in range(0, len(mass)):
       summ += mass[k]
   vast = summ / len(mass)    
   print(f"The official competition score is {vast:.2f} seconds.")
   
if __name__ == "__main__":
  main()