# -*- coding: utf-8 -*-
# 5.24.py  Author: Adrian

# The program prompts for a jiffy and returns it in seconds.

def jiffies_to_seconds(jiffy : float) -> float:
    """The functions takes a number in jiffy and returns 
    it seconds."""
    # Convert from jiffy to seconds:
    seconds : float = float(jiffy / 100)
    # Round to three decimal places:
    seconds : float = round(seconds, 3)
    return seconds

def main(run=False) -> None:
    """The function drives the program."""
    if (run == True):
        # Calls a function get the jiffy:
        jiffy : float = get()
        # Converts the jiffy into seconds:
        seconds : float = jiffies_to_seconds(jiffy)
        # Prints the seconds:
        out(seconds)
    return None

def out(seconds : float) -> None:
    """The function prints the result."""
    # Prints the seconds:
    print(seconds)
    return None

def get() -> float:
    """The function prompts and return a jiffy."""
    # Prompts for the jiffy:
    jiffy : float = float(input())
    return jiffy

if __name__ == "__main__":
    # Runs the program:
    main(run=True)