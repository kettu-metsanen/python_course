"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""

def main():

    filename = input("Enter the name of the file: ")
    try:
        file = open(filename, mode="r")
        i = 1
        for file_line in file:
            file_line = file_line.rstrip()
            print(i,file_line)
            i += 1
    
        file.close()
    except FileNotFoundError:
        print("There was an error in reading the file.")
if __name__ == "__main__":
    main()

