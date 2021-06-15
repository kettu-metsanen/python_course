"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""

LOAN_TIME = 3
MAX_LOANS = 3


class Librarycard:
    def __init__(self, card_id, card_holder):
        self.__id = card_id
        self.__holder = card_holder
        self.__books = {}
        self.__time = 0

    def holder(self):
        '''
        Palauttaa kortin omistajan nimen

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        return self.__holder

    def info(self):
        '''
        Tulostaa kortin omistajan nimen ja hanen lainaamat kirjat
        ja palautusajat

        Returns
        -------
        None.

        '''
        print("Card holder:", self.__holder)
        if len(self.__books) > 0:
            for book in sorted(self.__books):
                print(f"- Loan {book}, loan time left {self.__books[book]} weeks" )
        else:
            print("- No loans")
        
    def add_book(self, book):
        '''
        Tama metodi lisaa kirjan omistajan kortille ja
        maarittelee palautusajan

        Parameters
        ----------
        book : string
            kirjan koodi.

        Returns
        -------
        None.

        '''
        self.__books[book] = self.__time
        
    def get_books(self):
        '''
        Metodi palauttaa kortin kirjat.

        Returns
        -------
        dict
            Dict, jonka avain on kirjan koodi ja arvona on palautusajan.

        '''
        return self.__books
    
    def remove_books(self, num_book):
        '''
        Poistaa kirjan omistajan kortilta

        Parameters
        ----------
        num_book : string
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        del self.__books[num_book]

    def set_time(self, time):
        '''
        Asettaa kirjalle palautusajan

        Parameters
        ----------
        time : int
            palautusaika viikkoina.

        Returns
        -------
        None.

        '''
        self.__time = time
        
    def get_time(self):
        '''
        Palauttaa pitoajan
        '''
        return self.__time
        
        
def read_card_data(file_name):
    card_data = {}

    try:
        file_object = open(file_name, mode="r")

        for line in file_object:
            line = line.strip()
            strings = line.split(";")

            card_id = int(strings[0])
            card_holder = strings[1]

            new_card = Librarycard(card_id, card_holder)

            card_data[card_id] = new_card

    except OSError:
        print("Error in reading the file")
        return None

    return card_data


def read_card_id(prompt, database):
    while True:
        try:
            id = int(input(prompt))

            while id not in database:
                print("Erroneous card id, existing id's are:")
                listing(database)
                id = int(input(prompt))

            return id

        except ValueError:
            print("Erroneous card id, existing id's are:")
            listing(database)


def listing(cards):
    for card in sorted(cards):
        print(card, ":", cards[card].holder())

def book_check(cards, book):
    '''
    Metodi joka tarkistaa on kirja varattu vai ei. Jos kirja on hyllyssa,
    palauttaa nollan. Jos kirja on varattuu, metodi palauttaa kortin numeron
    jonka nimella kirja on varattu.

    Parameters
    ----------
    cards : tietorakenne, jossa on kaikki kortit
        DESCRIPTION.
    book : string
        kirjan koodi.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    for number in cards:
        if book in cards[number].get_books():
            return number
    return 0
    
def week(cards):
    '''
    Vahentaa kirjan pitoaikaa yhdella jos tama funktio on kutsuttu.

    Parameters
    ----------
    cards : tietorakenne, jossa kaikki kortit ovat
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    for number in cards:
        book_dic = cards[number].get_books()
        for i in book_dic:
            aika_nyt = book_dic[i]
            if aika_nyt != 0:
                book_dic[i] = aika_nyt-1
                cards[number].set_time(book_dic[i])
            
    
def main():
    library = read_card_data("library.txt")
    if library == None:
        return

    print("Welcome to Perähikiä library!")

    while True:
        command = input("Command: ")
        command = command.upper()

        if command == "I":
            card = read_card_id("Card code: ", library)
            library[card].info()

        elif command == "L":
            listing(library)

        elif command == "B":
            num_card = int(read_card_id("Card code: ", library))
            num_book = input("Book code: ")
            book_on = book_check(library, num_book) # tarkistaa onko kirja varattu
            if book_on == 0: # jos on hyllyssa
                if num_card in library:
                    if len(library[num_card].get_books()) == LOAN_TIME:
                        print(f"Card {num_card} has already {LOAN_TIME} loans")
                        print("Loan not successful")
                    else:
                        library[num_card].set_time(LOAN_TIME)
                        aika = library[num_card].get_time()
                        library[num_card].add_book(num_book)
                        
                        print(f"Loan successful, loan time {aika} weeks")
            else: # jos on varattu
                book_holder = library[book_on].holder()
                print(f"Customer {book_on} {book_holder} has already borrowed book with id {num_book}")

        elif command == "R":
            num_book = input("Book code: ")
            book_on = book_check(library, num_book)
            if book_on == 0:
                print("This book has not been borrowed by anyone")
            else:
                library[book_on].remove_books(num_book)
                print("Book returned")
        elif command == "W":
            week(library)
            print("Loan times updated!")

        elif command == "" or command == "Q":
            print("Thankyou and good bye!")
            return

        else:
            print("Erroneous command!")
            print("The commands are:")
            print("Info")
            print("List librarycards")
            print("Borrow")
            print("Return")
            print("new Week")


if __name__ == "__main__":
    main()
