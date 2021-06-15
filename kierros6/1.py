"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""

def main():
   glasnaya = 0
   sogls = 0
   sano = input("Enter a word: ")
   for i in range(len(sano)):
       if sano[i] == "a" or sano[i] == "e" or sano[i] == "i" or sano[i] == "o" or sano[i] == "u" or sano[i] == "y":
           glasnaya += 1
   sogls = len(sano) - glasnaya
   print(f'The word "{sano}" contains {glasnaya} vowels and {sogls} consonants.')
           
   
if __name__ == "__main__":
  main()