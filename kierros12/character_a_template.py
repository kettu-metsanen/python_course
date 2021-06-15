"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""

class Character:
    # TODO: the class implementation goes here.
    def __init__(self, name):
        
        self.__name = name
        self.__bagaj = {}
        
    def get_name(self):
        return self.__name
        
    def give_item(self, test_item):
        if test_item in self.__bagaj:
            self.__bagaj[test_item] += 1
        else:
            self.__bagaj[test_item] = 1
            
    def remove_item(self, item):
        if item in self.__bagaj:
            if self.__bagaj[item] == 1:
                del self.__bagaj[item]
            else:
                self.__bagaj[item] -= 1
    
    def has_item(self, item):
        if item in self.__bagaj:
            return True
        else:
            return False
        
    def how_many(self, item):
        if item in self.__bagaj:
            return self.__bagaj[item]
        else:
            return 0
        
    def printout(self):
        print('Name:', self.__name)
        if bool(self.__bagaj) == False:
            print("  --nothing--  ")
        for item in sorted(self.__bagaj):
            print(" ", self.__bagaj[item], item)
#%%        
def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")



if __name__ == "__main__":
    main()
