"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""


# TODO:
# a) Implement the class Player here.
class Player:
    
    def __init__(self, nimi):
        
        self.__nimi = nimi
        self.__ochki = 0
        self.__prozent_popadani = 0
        self.__avg = 0 
        self.__counter=0 
        self.__schet = 0
        
    def add_points(self, pts):
        self.__ochki += pts
        if self.__ochki >= 40 and self.__ochki <= 49:
            print(f"{self.__nimi} needs only {50-self.__ochki} points. It's better to avoid knocking down the pins with higher points.")
        self.ret_avg(pts)
        if self.__ochki > 50:
            print(f"{self.__nimi} gets penalty points!")
            self.__ochki = 25
        
    def get_name(self):
        
        return self.__nimi
    
    def get_points(self):
        
        return self.__ochki
    
    def has_won(self):
        
        if self.__ochki == 50:
            return True
        
    def prozent(self,pst):
       
            if pst > 0:
                self.__schet += 1
                self.__prozent_popadani = self.__schet /self.__counter * 100
                
            else:
                self.__prozent_popadani = self.__schet /self.__counter * 100
                
        
            
    def get_proc(self):
        
        return self.__prozent_popadani
    
    def ret_avg(self, pts):
        if self.__ochki <= 50:
            self.__counter += 1
            if self.__counter >= 2:
                self.__avg = self.__ochki / self.__counter
                if self.__avg < pts:
                    print(f"Cheers {self.__nimi}!")
        else:
            self.__counter += 1
            

def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))
        # if in_turn.ret_avg(pts):
        #     print(f"Cheers {in_turn.get_name()}!")
        
        in_turn.add_points(pts)

        # TODO:
        # c) Add a supporting feedback printout "Cheers NAME!" here.
        in_turn.prozent(pts)

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(f"{player1.get_name()}: {player1.get_points()} p, hit percentage {player1.get_proc():.1f}")  # TODO: d)
        print(f"{player2.get_name()}: {player2.get_points()} p, hit percentage {player2.get_proc():.1f}")  # TODO: d)
        print("")

        throw += 1


if __name__ == "__main__":
    main()
