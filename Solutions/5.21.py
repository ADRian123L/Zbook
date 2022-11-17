# -*- coding: utf-8 -*-
# 5.21  Author:  Adrian

# The program prompts for a decimal numbers and returns it in binary.

def main() -> None:
    """The function runs the program."""
    integers = inputs()
    reversed_binary = int_to_reverse_binary(integers)
    binary = string_reverse(reversed_binary)
    output(binary)
    return None

def int_to_reverse_binary(decimal : int) -> str:
    """The functions returns a string representing a decimal number 
    in binary."""
    # An empty list to store the binary numbers:
    bin = list()
    # Transforms the decimal into a binary:
    done = False
    if (decimal <= 0):
        bin.append(0)
    else:
        done = True
    while done:
        mod = decimal % 2
        bin.append(mod)
        decimal //= 2
        if (decimal <= 0):
            done = False
    # Converts the list into a string:
    binary = lambda lists: "".join(str(i) for i in lists[:])
    return binary(bin)

def string_reverse(string : str) -> str:
    """The function returns the reversed order of a string."""
    # Reverses the order of the string:
    string = "".join((reversed(string)))
    return string

def inputs() -> int:
    """The function prompts for an integer and returns it."""
    # Prompts for an integer:
    integers = int(input())
    return integers

def output(binary : str) -> None:
    """The function prints its argument."""
    # Prints the argument:
    print(binary)
    return None

if __name__ == "__main__":
    # Runs the program:
    main()