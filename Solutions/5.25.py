# -*- coding: utf-8 -*-
# 10.11.py  Author: Adrian

# The program prompts for a year and returns wether it is
# a leap year or not.

# variables:
out : list = [" has ", " days in February."]

# Functions:
def days_in_feb(year : int) -> float:
    """The function takes a year and determines wether it
    is leap year."""
    # Local variable:
    is_leap : bool = False
    # Checks if there are any arguments:
    try:
        year *= 1
    except:
        year : int = info() # Calls the function.
        # # Checks if it is a leap year:
    if (year % 4 == 0):
        if (year % 100 == 0):
            is_leap = (True if (year % 400 == 0) else is_leap)
        else:
            is_leap = True
    # Sets how many days the year has:
    days : int = (29 if (is_leap == True) else 28)
    # Formats the output:
    format : str = f"{year}{out[0]}{days}{out[1]}"
    return format

def output(format : str) -> None:
    """The function prints the answer."""
    print(format)
    return None


def info() -> int:
    """The function prompts for a year and returns it."""
    year : int = int(input())
    return year

def main(run=False) -> None:
    """The function drives the program."""
    format : str = days_in_feb(None) # Calls the function:
    output(format)
    return None

if __name__ == "__main__":
    main(run=True)