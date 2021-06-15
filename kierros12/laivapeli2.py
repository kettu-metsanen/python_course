"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
class Submarine:
    '''
    Luokka, joka esittää pelilaudalla olevan laivan.
    Sisäiset muuttujat:
        name - laivan nimi(string)
        coords - laivan koordinaatit. Jos laiva koostu 4sta osasta niin
                tämä sisältää 4 koordinaattia (string)
        hits - montako kertaa laivaan osuttiin (int)
        state - onko laiva upotettu vai ei (bool)
    '''
    def __init__(self, name, size, coords):
        """
        Luokan alustaminen.

        Parameters
        ----------
        name : string
            Laivan nimi
        size : int
            Laivan koko
        coords : string
            Laivan kaikkien osien koordinaatit

        Returns
        -------
        None.

        """
        self.__name = name
        self.__size = size
        self.__coords = coords
        self.__hits = 0
        self.__state = 0
        
    def decode_coordinates(self):
        """
        Apufunktio, jota käytetään koordinaattien muunnosta varten
        muodosta "[kirjain],[luku]" muotoon "[luku], [luku]".

        Returns
        -------
        decoded : list
            Jos laivan koko on 1 niin palautuu yksi lista, jossa on vain
            kaksi koordinaattia. Jos laivan koko on enemmän kuin 1,
            funktion palauttaa listan, joka sisältää jokaisen
            laivan osan koordinaatit, eli listan listassa.

        """
        decoded = []
        bcoord = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7,
                  'I':8, 'J':9}
        for c in self.__coords:
            x,y = c[0],int(c[1])
            x = bcoord[x]
            decoded.append([x,y])
        return decoded
    
        
    def check_status(self):
        """
        Funktio tarkistaa onko laiva upotettu vai ei

        Returns
        -------
        None.

        """
        if self.__hits == self.__size:
            self.__state = 1   
        return
    
    def set_hit(self):
        """
        Funktio laskee kuinka monta kertaa laivaan osuttiin ja kasvattaa
        laskuria. Jos laskurin arvo on sama kuin laivan koko, niin
        laiva on upotettu

        Returns
        -------
        None.

        """
        if self.__state != 1:
            self.__hits += 1
            self.check_status()
        return
    
    def get_status(self):
        """
        Palauttaa laivan tilan "upotettu/ei upotettu"

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.__state
    
    def get_coords(self):
        """
        Palauttaa laivan koordinaatit

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.__coords
    def get_name(self):
        """
        Palauttaa laivan nimen

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self.__name
        
class Playground:
    """
    Tämä luokka vastaa pelialueelta. Välittää iskut laivoille,
    määrittelee voittajan jne.
    """
    def __init__(self, submarine):
        """
        Lukan alustaminen. Sisäiset muuttujat:
            size - pelialueen koko
            board - sisältää listojen listan, jossa on kaikki
                tarvittavat merkit.
            submarines - sisätlää vektorin, jossa on kaikki
                pelissa osallistuvat laivat (submarine-luokan edustajat)
            coord - sisäiseen käyttöön tarkoitettu dicti, jossa jokaisen koordinaatin
                kirjain muutetaan luvuksi.

        Parameters
        ----------
        submarine : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.__size = 10
        self.__board = []
        self.__submarines = submarine
        for i in range(10):
            self.__board.append([" "]*10)
        self.__coords = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}
        
    def hit(self, coord):
        """
        Välittää osumiset laivoille, t.s. kasvattaa tietyn laivan
        hit-laskuria. Jos osumaa ei ollut sijoittaa pelialueelle
        "ohi"-merkin. Jos laiva on upotettu sijoittaa pelialueelle
        tietyn lavan nimen ensimmainen kirjain.

        Parameters
        ----------
        coord : string
            Koordinaatti muodossa [kirjain,luku]

        Returns
        -------
        None.

        """
        x, y = self.__coords[coord[0]], int(coord[1])
        for sub in self.__submarines:
            if [x,y] in sub.decode_coordinates():
                if self.__board[y][x] != ' ':
                    print("Location has already been shot at!")
                else:
                    self.__board[y][x] = 'X'
                    sub.set_hit()
                    nimi = sub.get_name()
                    kirja = nimi[0].upper()
                    if sub.get_status() == 1:
                        for [x,y] in sub.decode_coordinates():
                            self.__board[y][x] = kirja
                        print(f"You sank a {nimi}!")
                #break
                return
        if self.__board[y][x] == '*':
            print("Location has already been shot at!")
        else:    
            self.__board[y][x] = '*'
            #break
    
    def print_board(self):
        """
        Hoitaa pelialueen tulostamisen näytölle.

        Returns
        -------
        None.

        """
        print()
        updownstring = "  A B C D E F G H I J"
        print(updownstring)
        for i in range(10):
           print(i," "," ".join(self.__board[i])," ",i,sep="")
        print(updownstring)
        print()
    
                
    def check_play(self):
        """
        Funktio tarkistaa onko pelaaja voittanut. Palauttaa True jos on voitto.

        Returns
        -------
        bool
            DESCRIPTION.

        """
        counter = 0 
        for sub in self.__submarines:
            if sub.get_status() == 1:
                counter += 1
        if counter == len(self.__submarines):
            return True
        
        
def check_input_validity(command):
    '''
    Tarkistaa syötetyn koordinaatin. Jos koordinaatti ei noudata
    alla mainittuja ehtoja funktio palauttaa False, muussa tapauksessa
    palauttaa True

    Parameters
    ----------
    command : string
        käyttäjän syöttämä koordinaatti

    Returns
    -------
    bool
        True, jos koordinaatti oli oikein
        False, jos ei ollut oikein.

    '''
    if len(command) != 2:
        if command == 'Q':
            return True
        else:
            return False
    if command[0] not in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"] \
        or command[1] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]:
        return False
    return True
        
    
        
            
def main():
    try:
        fname = input("Enter file name: ")
        #fname = 'laivat.txt'
        subs = []
        coords_maara = []
        sopi_kirjat = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        sopi_luvut = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
        
        with open(fname, 'r') as fl:
            battlelist = fl.readlines()
            
        for row in battlelist:
            subrow = row.strip().split(";")
            name = subrow[0]
            size = len(subrow[1:])
            coords = subrow[1:]
            for i in coords: # tiedostossa olevien koordinaattien tarkastus
                if (i[0] not in sopi_kirjat) or (i[1:] not in sopi_luvut):
                    print("Error in ship coordinates!")
                    return
                coords_maara.append(i)
            subs.append(Submarine(name, size, coords))
        if len(coords_maara) != len(set(coords_maara)): 
            print("There are overlapping ships in the input file!")
            return
        
        board = Playground(subs)
        board.print_board()
            
        paikka = input("Enter place to shoot (q to quit): ")
        paikka_hit = paikka.upper()

        while not check_input_validity(paikka_hit):
            print("Invalid command!")
            board.print_board()
            paikka = input("Enter place to shoot (q to quit): ")
            paikka_hit = paikka.upper()

        while paikka_hit != "Q":

            board.hit(paikka_hit)
            board.print_board()
            if board.check_play() == 1:
                print("Congratulations! You sank all enemy ships.")
                return
            paikka = input("Enter place to shoot (q to quit): ")
            paikka_hit = paikka.upper()

            while not check_input_validity(paikka_hit):
                print("Invalid command!")
                board.print_board()
                paikka = input("Enter place to shoot (q to quit): ")
                paikka_hit = paikka.upper()

        print("Aborting game!") 
    
    except IOError:
        print("File can not be read!")
if __name__ == "__main__":
    main()