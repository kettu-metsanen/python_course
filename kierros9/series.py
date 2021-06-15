"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
seri"""

def read_file(filename):
    """
    Reads and saves the series and their genres from the file.

    TODO: comment the parameter and the return value.
    """

    series_list = {}

    try:
        file = open(filename, mode="r")

        for row in file:

            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")
            
            genres = genres.split(",")

            series_list[name] = genres

        file.close()
        return  series_list

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)
    
    test_list = list()
    for name in genre_data:
        for i in range(len(genre_data[name])):
            if genre_data[name][i] not in test_list:
                test_list.append(genre_data[name][i])
    sort_list = sorted(test_list)
    print("Available genres are: ",end="")
    for i in sort_list:
        if i == sort_list[-1]:
            print(i)
        else:
            print(i, ", ",sep="", end="")
    
    spisok = list()
    while True:
        genre = input("> ")

        if genre == "exit":
            return

        for ima, nazv_janra in genre_data.items():
            if genre in nazv_janra:
                spisok.append(ima)
        for film in sorted(spisok):
            print(film)
        spisok = list()
if __name__ == "__main__":
    main()
