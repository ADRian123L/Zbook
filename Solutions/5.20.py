# 5.20.py  Author: Adrian

# The program prompts for the miles walked and returns the number of
# steps taken.

# The function:
def feet_to_steps(feet : float) -> int:
    """The function takes the an amount in foots and returns the number 
    of steps take."""
    steps = feet / 2.5
    steps = int(steps) 
    return steps

def reed() -> float:
    """The function prompts for the number of foots and returns
    the input as a floating-point number."""
    feet = float(input())
    return feet

def main() -> None:
    """The function runs the program."""
    feet = reed()
    steps = feet_to_steps(feet)
    print(steps)
    return None

if __name__ == "__main__":
    main()