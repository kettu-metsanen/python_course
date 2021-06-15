"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
class Submarine:
    def __init__(self, name, size, coords, mark = 0):
        self.__name = name
        self.__size = size
        self.__coords = coords
        self.__mark = mark
    
    def get_coords(self):
        return self.__coords
    def get_name(self):
        return self.__name
    def get_size(self):
        return self.__size
    def get_mark(self):
        return self.__mark
    def set_mark(self, new_mark):
        self.__mark = new_mark

class PlayBoard:
    def __init__(self):
        self._board = []
        for i in range(10):
            self._board.append([" "]*10)
        self._coords = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}
        self.__fill_cont = []
        self.__submarine = []

        
    def print_board(self):#pechat doskii
        
        mass_nimi = []
        for sub in self.__submarine:
                mark = sub.get_mark()
                size = sub.get_size()
                nimi = sub.get_name()
                kirja = nimi[0]
                #ret_nimi = ""
                if mark == size: 
                    ret_nimi = nimi
                    mass_nimi.append(ret_nimi)
                    place = sub.get_coords()
                    for pair in place:
                        x,y = self.parse_coordinate(pair)
                        self._board[y][x] = kirja.upper()
                    return "2", ret_nimi
        updownstring = "  A B C D E F G H I J "
        print(updownstring)
        for i in range(10):
           print(i," "," ".join(self._board[i])," ",i,sep="")
        print(updownstring)
        #if ret_nimi != "":
            #print("You sank a ", ret_nimi,"!", sep="")
        if len(mass_nimi) == len(self.__submarine):   
            return "1", 0
        else:
            return "0", 0
        
        
    def parse_coordinate(self, coord):
        
        x = self._coords[coord[0]]
        y = coord[1]
        return int(x), int(y)
        
    def add_to_board_yes(self, cord):#esli popalo v mesto probela X
        
        x,y = self.parse_coordinate(cord)
        self._board[y][x] = "X"
        
        
        
    def add_to_board_no(self, cord):#ne popali *
        
        x,y = self.parse_coordinate(cord)
        self._board[y][x] = "*"
        
    def fill(self, submarin):#v massiv zabivaem raspolojenie vsex korablei
        self.__submarine.append(submarin)
        place = submarin.get_coords()
        for pair in place:
            self.__fill_cont.append(pair)
        
    
    def check(self, cord):#proveraem est li tut korabl
        for sub in self.__submarine:
            all_cord = sub.get_coords()
            
            if cord in all_cord:
               
                mark = sub.get_mark()
                sub.set_mark(int(mark)+1)
        if cord in self.__fill_cont:
            self.add_to_board_yes(cord)
        else:
            self.add_to_board_no(cord)

    def location_check(self, cord): #proveraem bila li yje eta koordinata
        x,y = self.parse_coordinate(cord)
        if self._board[y][x] != " ":
            return False
        
   
def main():
    #fname = input("Enter file name:")
    fname = 'laivat.txt'
    subs = []
    sopi_kirjat = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    sopi_luvut = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
    mass = []
    try:#proveraem fail na otkritie
        with open(fname, 'r') as fl:
            battlelist = fl.readlines()
        for row in battlelist:
            subrow = row.strip().split(";")
            name = subrow[0]
            size = len(subrow[1:])
            coords = subrow[1:]
            for i in coords: #proveraem na sootvetstvie koordinatnoi setki
                if (i[0] not in sopi_kirjat) or (i[1] not in sopi_luvut):
                    print("Error in ship coordinates!")
                    return
                mass.append(i)
            subs.append(Submarine(name, size, coords))
        if len(mass) != len(set(mass)):#proveraem na odinakovie koordinati
            print("There are overlapping ships in the input file!")
            return
        
        board = PlayBoard()
        vime, vin_nimi = board.print_board()
        
        
        for i in range(len(subs)):#zapolnaem koroblami
            board.fill(subs[i])
        try:#proverka na pravilnuyu komandu
            test = input("Enter place to shoot (q to quit): ")
            coord = test.upper()
        except KeyError:
            print("Invalid command!")
        while coord != "Q":
            try:#proverka na pravilnuyu komandu
                if board.location_check(coord) == 0:#proveraem bila li yje eta koordinata
                    print("Location has already been shot at!")
                    test = input("Enter place to shoot (q to quit): ")
                    coord = test.upper()
                board.check(coord)
                vime, vin_nimi = board.print_board()
                if vime == "1":
                    print("Congratulations! You sank all enemy ships.")
                    return
                elif vime == "2":
                    print("You sank a ", vin_nimi,"!", sep="")
                elif vime == "0":
                    continue
                test = input("Enter place to shoot (q to quit): ")
                coord = test.upper()
                
            except KeyError:
                print("Invalid command!")
                test = input("Enter place to shoot (q to quit): ")
                coord = test.upper()
        print("Aborting game!") 
    except IOError:
        print("File can not be read!")
    
    
    
if __name__ == "__main__":
    main()