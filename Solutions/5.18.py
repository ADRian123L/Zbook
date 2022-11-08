# -*- coding: utf-8 -*-
# 5.18.py  Author: Adrian

# The program prompts for a weight in kilo and returns the value in
# pounds.

# Constant:
POUNDS = 2.204

# The function that converts form kilos to pounds:
def kilo_to_pounds(kilos : float) -> float:
    """The function returns a weight in pounds."""
    pounds = kilos * POUNDS
    return pounds

if __name__ == "__main__":

    # Prompts for the weight in kilos:
    try:
        kilos = float(input())
    except:
        kilos = 1

    # Converts to pounds:
    pounds = kilo_to_pounds(kilos)

    # Outputs the result:
    print(f"{pounds:.3f} lbs")

    