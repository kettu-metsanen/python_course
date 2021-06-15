"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""

def main():
    yht = dict()
    nimifail = input("Enter the name of the score file: ")
    
    try:
        file = open(nimifail, mode="r")
        for file_line in file:
            #try:
            file_line = file_line.rstrip()
            game_list = file_line.split()
            if len(game_list) != 2:
                #continue
            #except:
                print("There was an erroneous line in the file:")
                print(file_line)
                return
            if game_list[0] in yht:
                try:
                    yht[game_list[0]] += int(game_list[1])
                except ValueError:
                    print("There was an erroneous score in the file:")
                    print(game_list[1])
                    return
            else:
                try:
                    yht[game_list[0]] = int(game_list[1])
                except ValueError:
                    print("There was an erroneous score in the file:")
                    print(game_list[1])
                    return
        for word in sorted(yht):
            print(word, yht[word])     
        file.close()
    except:
        print("There was an error in reading the file.")
        return
if __name__ == "__main__":
    main()
"""
essi 5
pietari 9
essi 2
pietari 10
pietari 7
aps 25
essi 1
"""
