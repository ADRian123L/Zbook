# -*- coding: utf-8 -*-
# 5.22 Author:  Adrian

# The program prompts for four integers and return the integers in a
# different order.


def main() -> None:
    """The function runs the program."""
    # Executes  the program:
    numbers = inputs()
    swap_values(numbers[0], numbers[1], numbers[2], numbers[3])
    return None

def inputs() -> list:
    """The function prompts for four integers and returns them."""
    # Prompts for the integers:
    numbers = list()
    for inputs in range(4):
        integers = int(input())
        numbers.append(integers)
    return numbers

def swap_values(*args : int) -> None:
    """The function takes four arguments and returns them at a different
    order."""
    # Reorganizes the order of the numbers:
    numbers = list(args[:])
    second = numbers.pop(0)
    numbers.insert(1, second)
    fourth = numbers.pop(2)
    numbers.insert(3, fourth)
    output(numbers)
    return numbers[0], numbers[1], numbers[2], numbers[3]

def output(number : list) -> None:
    """The function takes a list and prints it."""
    number = " ".join(str(i) for i in number[:])
    print(number)
    return None

if __name__ == "__main__":
    # Starts the program:
    main()