# -*- coding: utf-8 -*-
# 5.25.py  Author: Adrian

# The program prompts for the number of laps and returns
# the miles run.

# Constant:
ONE_LAP : float = 0.25

# The functions:
def main(run=False) -> None:
    """The function drives the program."""
    if (run == True):
        # Prompts:
        laps : float = lap()
        # Calculates:
        miles : float = laps_to_miles(laps)
        # Prints:
        output(miles)
    return None

def laps_to_miles(laps : float) -> float:
    """The function returns the miles run."""
    # Converts from laps to miles:
    miles : float = laps * ONE_LAP
    miles = round(miles, 2)
    return miles

def lap() -> float:
    """The function prompts for the number of laps."""
    # Prompts for the number of laps:
    laps : float = float(input())
    return laps

def output(miles : float) -> None:
    """The function prints the number of miles."""
    # Changes to number to two decimal places:
    miles = f"{miles:.2f}"
    # Prints the number:
    print(miles)
    return None

if __name__ == "__main__":
    main(run=True)