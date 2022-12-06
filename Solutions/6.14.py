"""
    Author: Adrian
    6.14.py
    The program prompts for the caffein level
    in the blood. And outputs the caffeine levels
    after some hours.
"""

# The output messages:
format = [
    "After 6 hours:",
    "After 12 hours:",
    "After 24 hours:"
]

# Hours:
hours = [6, 12, 24]

# Functions:
def main(run=False) -> None:
    """The function drives the program."""
    if (run == True):
        # Prompts for a number:
        number : int = get()
        # Calculates caffeine levels at each period:
        get_list : list = calculate(number)
        # Prints the results:
        out(get_list)
    return None

def out(levels : list) -> None:
    """The function prints the results."""
    # Prints the results formatted:
    for index, numbers in enumerate(levels):
        formatting = f"{format[index]} {numbers:.2f} mg"
        print(formatting)
    return None

def get() -> float:
    """The function prompts for the caffeine."""
    # Prompts for the caffeine:
    number : float = float(input())
    return number

def calculate(number : float) -> float:
    """The function calculates the caffeine levels."""
    # Empty list:
    levels : list = list()
    # Calculates the levels:
    for i in hours[:]:
        levels.append((number * ((.5)**(i/6))))
    return levels

if __name__ == "__main__":
    main(run=True)