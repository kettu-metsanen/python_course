"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    
    thing = input("Enter product name: ")
    thing_new = thing.strip()
    while thing_new != "":
        
        if thing_new in PRICES:
            print(f"The price of {thing_new} is {PRICES[thing_new]:.2f} e")
        elif thing not in PRICES:
            print(f"Error: {thing_new} is unknown.")
        thing = input("Enter product name: ")
        thing_new = thing.strip()
    print("Bye!")
    pass


if __name__ == "__main__":
    main()
