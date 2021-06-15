"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    print("Dictionary contents:")
    new_engl = sorted(english_spanish)
    print(", ".join(new_engl))
    while True:
        
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            thing = input("Enter the word to be translated: ")
            if thing not in english_spanish:
                print("The word", thing, "could not be found from the dictionary.")
            else:
                print(f"{thing} in Spanish is {english_spanish[thing]}")
            

        elif command == "A":
            po_eng = input("Give the word to be added in English: ")
            po_span = input("Give the word to be added in Spanish: ")
            english_spanish[po_eng] = po_span
            print("Dictionary contents:")
            new_engl = sorted(english_spanish)
            print(", ".join(new_engl))
            
        elif command == "R":
            udal = input("Give the word to be removed: ")
            if udal in english_spanish:
                del english_spanish[udal]
            else:
                print(f"The word {udal} could not be found from the dictionary.")
                
        elif command == "P":
            print()
            print("English-Spanish")
            for word in sorted(english_spanish):
                print(word, english_spanish[word])
            print()
            print("Spanish-English")
            list_keys = list(english_spanish.items())
            list_keys.sort(key=lambda i: i[1])
            for i in list_keys:
                print(i[1], i[0])
            print()
        elif command == "T":
            text = input("Enter the text to be translated into Spanish: ")
            text_razd = text.split()
            obsh_text = ""
            for i in range(0, len(text_razd)):
                if i == len(text_razd) - 1:
                    if text_razd[i] in english_spanish:
                        obsh_text += english_spanish[text_razd[i]]
                    else:
                        obsh_text += text_razd[i]
                else:    
                    if text_razd[i] in english_spanish:
                        obsh_text += english_spanish[text_razd[i]] + " "
                    else:
                        obsh_text += text_razd[i] + " "
            print("The text, translated by the dictionary:")
            print(obsh_text)
            
        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
