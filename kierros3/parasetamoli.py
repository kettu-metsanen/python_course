"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def calculate_dose(massa, hours, milligramm):
    """lasku paljonko sää vielä parasetamolia"""
    maxDoza = 15 * massa
    if hours < 6:
        return 0
    else:
        lasku = 4000 - milligramm
        if maxDoza <= lasku:
            return maxDoza
        else:
            return lasku
def main():
    ves = int(input("Patient's weight (kg): "))
    chasi = int(input("How much time has passed from the previous dose (full hours): "))
    doza = int(input("The total dose for the last 24 hours (mg): "))
    rezult = calculate_dose(ves, chasi, doza)
    print("The amount of Parasetamol to give to the patient:", rezult)

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)


if __name__ == "__main__":
  main()
