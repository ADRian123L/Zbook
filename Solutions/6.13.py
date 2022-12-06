# -*- coding: utf-8 -*-
# 6.13.py  Author: Adrian

# The program takes an input integer and returns is as
# phone number.


# Function:

def main() -> None:
    """The function drives the program."""
    number : int = get_number()
    phone : str = convert(number)
    out(phone)
    return None

def out(phone : str) -> None:
    """The functions prints."""
    print(phone)
    return None

def get_number() -> int:
    """The function prompts for an integer and
    returns int."""
    number = int(input())
    return number
    
def convert(number : int) -> str:
    """The functions returns a string formatted as a
    phone number."""
    number = str(number)
    first : str = number[0:3]
    second : str = number[3:6]
    third : str = number[6:]
    format : str = f"({first}) {second}-{third}"
    return format

if __name__ == "__main__":
    main()