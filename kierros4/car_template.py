"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""

from math import sqrt


def menu():
    """
    This is a text-based menu. You should ONLY TOUCH TODOs inside the menu.
    TODOs in the menu call functions that you have implemented and take care
    of the return values of the function calls.
    """

    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(gas, tank_size, to_fill)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x, y, new_x, new_y, gas, gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")


def fill(ckolko_seichas, skolko_vmeshaet, skolko_hotat_dobavit):
    """
    This function has three parameters which are all FLOATs:
      (1) the size of the tank
      (2) the amount of gas that is requested to be filled in
      (3) the amount of gas in the tank currently

    The parameters have to be in this order.
    The function returns one FLOAT that is the amount of gas in the
    tank AFTER the filling up.

    The function does not print anything and does not ask for any
    input.
    """
    
    vast = ckolko_seichas + skolko_hotat_dobavit
    if vast > skolko_vmeshaet:
        return skolko_vmeshaet
    else:
        return vast


def drive(seichas_x, seichas_y, hotim_x, hotim_y, seichas_gas, rashod_gas):
    """
    This function has six parameters. They are all floats.
      (1) The current x coordinate
      (2) The current y coordinate
      (3) The destination x coordinate
      (4) The destination y coordinate
      (5) The amount of gas in the tank currently
      (6) The consumption of gas per 100 km of the car

    The parameters have to be in this order.
    The function returns three floats:
      (1) The amount of gas in the tank AFTER the driving
      (2) The reached (new) x coordinate
      (3) The reached (new) y coordinate

    The return values have to be in this order.
    The function does not print anything and does not ask for any
    input.
    """
    skolko_proedem = raschet_skolko_proedem(seichas_x, seichas_y, hotim_x, hotim_y)
    potratim_benza = raschet_benza(rashod_gas, skolko_proedem)
    vozvrat_gaza = seichas_gas - potratim_benza
    return vozvrat_gaza, hotim_x, hotim_y
    
    # It might be usefull to make one or two assisting functions
    # to help the implementation of this function.
def kakie_koordinati(kord_x_star, kord_y_star, kord_x_now, kord_y_now, put):
    
    dlin_x = kord_x_now - kord_x_star
    dlin_y = kord_y_now - kord_y_star
    p = dlin_y / dlin_x * put
    
    
def skolko_mogno_proehat(benz, rashod):
    
    skolko_hvatit = rashod / 100 / benz
    return skolko_hvatit
    
def raschet_skolko_proedem(kord_x_star, kord_y_star, kord_x_now, kord_y_now, benz, rashod ):
    """ lasku mika matka on ja paljonko se on kilometria"""
    dlin_x = kord_x_now - kord_x_star
    dlin_y = kord_y_now - kord_y_star
    proedem = sqrt(dlin_x * dlin_x + dlin_y * dlin_y)
    skolko_mojem = skolko_mogno_proehat(benz, rashod)
    if skolko_mojem > proedem:
        return proedem
    else:
        return skolko_mojem
    
def raschet_benza(zatrata, skolko_proedem):
    """lasku paljonko pitää gas ja mita return"""
    vivod = zatrata / 100 * skolko_proedem
    return vivod

def read_number(prompt, error_message="Incorrect input!"):
    """
    DO NOT TOUCH THIS FUNCTION.
    This function reads input from the user.
    Also, don't worry if you don't understand it.
    """

    try:
        return float(input(prompt))

    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


if __name__ == "__main__":
    main()
