# -*- coding: utf-8 -*-
# 5.19.py  Author: Adrian

# The program prompts for three values and returns the cost of driving
# for 10, 50, and 400 miles.

# Constants:
MILE1, MILE2, MILE3 = 10, 50, 400

# The functions returns the cost of driving certain miles:
def driving_cost(mpg : float, ppg : float, miles : float) -> float:
    """The functions returns the cost of driving."""
    gallons = (1 / mpg) * (ppg)
    price = miles * gallons
    return price

if __name__ == "__main__":
    # Prompt for the miles per gallons and price per gallon:
    try:
        mile_p_gallon = float(input())
        price_p_gallon = float(input())
    except:
        mile_p_gallon = 20.0
        price_p_gallon = 3.1599
        miles = 50.0
    
    # Calculate the price:
    price1 = driving_cost(mile_p_gallon, price_p_gallon, MILE1)
    price2 = driving_cost(mile_p_gallon, price_p_gallon, MILE2)
    price3 = driving_cost(mile_p_gallon, price_p_gallon, MILE3)

    # Print the results:
    print(f"{price1:.2f}")
    print(f"{price2:.2f}")
    print(f"{price3:.2f}")