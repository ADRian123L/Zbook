# 4.16.py  Author: Adrian

# The program pomps for an integer and resturns the reverse of it's
# corresponding binary number.

# The function resturns the binary number in reverse:
def binary(input) -> int:
    bin = ""
    # Converts from decimal to reverse binary.
    while (input >= 1): 
        calculation = (input % 2)
        bin += str(calculation)
        input //= 2
    return (bin)

# Calls and outputs the result:
integer = int(input())
print(binary(integer))