"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Anna Rumiantseva
Opiskelijanumero: 050309159
"""
def input_list(day):
    """
    
    Parameters
    ----------
    day : moneltakon päivältä mittauksia kirjataan

    Returns
    -------
    temperature : list missä on kaikki temperaturit 

    """
    temperature = []
    for i in range(1, day+1):
        temperature.append(float(input(f"Enter day {i}. temperature in Celcius: ")))
    return temperature

def calculate_mean(list_temp):
    """

    Parameters
    ----------
    list_temp : list missä on kaikki temperaturit 

    Returns
    -------
    result : mean

    """
    
    summa = 0
    for i in range(0, len(list_temp)):
        summa += list_temp[i]
        i += 1
    result = summa / len(list_temp)
    return result

def calculate_median(list_temp):
    """
    

    Parameters
    ----------
    list_temp : list missä on kaikki temperaturit 

    Returns
    -------
    median 

    """
    sort_list_temp = sorted(list_temp)
    if len(list_temp) == 1:
        median = sort_list_temp[0]
        return median
    elif len(list_temp) % 2 == 0:
        index_median = len(list_temp) // 2             
        median = (sort_list_temp[index_median] + sort_list_temp[index_median-1]) / 2
        return median
    elif len(list_temp) % 2 != 0:
        index_median = len(list_temp) // 2
        median = sort_list_temp[index_median]
        return median
        
def over_median(mean, median, list_temp):
    """

    Parameters
    ----------
    mean, median
    list_temp : list missä on kaikki temperaturit 

    Returns
    -------
    print kaikki temperaturit isompi mean ja heidän ero

    """
    for i in range(0, len(list_temp)):
        if list_temp[i] >= median:
            print(f"Day{i+1:3.0f}.{list_temp[i]:6.1f}C difference to mean:{list_temp[i] - mean:6.1f}C")
        
    
def under_median(mean, median, list_temp):
    """

    Parameters
    ----------
    mean, median
    list_temp : list missä on kaikki temperaturit 

    Returns
    -------
    print kaikki temperaturit piempi mean ja heidän ero

    """
    for i in range(0, len(list_temp)):
        if list_temp[i] < median:
            print(f"Day{i+1:3.0f}.{list_temp[i]:6.1f}C difference to mean:{list_temp[i] - mean:6.1f}C")
        
def main():
   
    number_day = int(input("Enter amount of days: "))
    list_day = input_list(number_day)
    mean = calculate_mean(list_day)
    median = calculate_median(list_day)
    print(f"Temperature mean: {calculate_mean(list_day):.1f}C")
    print(f"Temperature median: {calculate_median(list_day):.1f}C")
    print("Over or at median were:")
    over_median(mean, median, list_day)
    print("Under median were:")
    under_median(mean, median, list_day)
    
if __name__ == "__main__":
  main()