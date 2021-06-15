"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""

def main():
    filename = input("Enter the name of the file: ")
    i = 1
    try:
        save_file = open(filename, mode="w")

    except OSError:
        print(f"Writing the file {filename} was not successful.")
        return

    print("Enter rows of text. Quit by entering an empty row.")

    while True:
        text_line = input()

        if text_line == "":
            break

        print(i, text_line, file=save_file)
        i += 1
    save_file.close()

    print(f"File {filename} has been written.")
if __name__ == "__main__":
    main()

