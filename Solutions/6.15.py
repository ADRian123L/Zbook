"""
    Author: Adrian
    6.15.py
    The program prompts for two integers. And
    returns the change in housing price and mortgage
    rate.
"""

# The output strings:
strings : dict = {
    0 : ["This house is ", ". The change is $", " since the last month."],
    1 : "The estimated monthly mortgage is $"
}

# The functions:
def main() -> None:
    """The function drives the program."""
    prices : int = get()
    calculations : list = calculate(*prices)
    output(prices[0], *calculations)
    return None

def output(*args : any) -> None:
    """The function prints the results."""
    format : str = f"{strings[0][0]}{args[0]}{strings[0][1]}{args[1]}{strings[0][2]}\n"
    format += f"{strings[1]}{args[2]}."
    print(format)
    return None

def get() -> list:
    """The function prompts for two integers
    and returns them in a list."""
    prices : int = list()
    for numbers in range(2):
        get = int(input())
        prices.append(get)
    return prices

def calculate(*args : int) -> list:
    """The function returns the change in price
    of a house and the monthly payment."""
    change : int = args[1] - args[0]
    mortgage : float = (args[0] * 0.051) / 12 
    return change, mortgage

if __name__ == "__main__":
    main()