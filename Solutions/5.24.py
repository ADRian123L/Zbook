# -*- coding: utf-8 -*-
# 10.11.py  Author: Adrian

# The program prompts for a year and returns wether it is
# a leap year or not.

def jiffies_to_seconds(jiffy : float) -> float:
    """The functions takes a number in jiffy and returns 
    it seconds."""
    seconds : float = float(jiffy / 100)
    seconds : float = round(seconds, 3)
    return seconds

def main(run=False) -> None:
    """The function drives the program."""
    if (run == True):
        jiffy : float = get()
        seconds : float = jiffies_to_seconds(jiffy)
        out(seconds)
    return None

def out(seconds : float) -> None:
    """The function prints the result."""
    print(seconds)
    return None

def get() -> float:
    """The function prompts and return a jiffy."""
    jiffy : float = float(input())
    return jiffy

if __name__ == "__main__":
    main(run=True)