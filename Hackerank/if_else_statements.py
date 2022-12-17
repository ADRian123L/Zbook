#!/bin/python3

import math
import os
import random
import re
import sys

def output(n : int) -> None:
    """The functions prints a statement depending
    on the parameter given."""
    if (n % 2 != 0):
        print("Weird")
    elif (n in range(2, 5)):
        print("Not Weird")
    elif (n in range(6, 21)):
        print("Weird")
    else:
        print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    # Calls the function:
    output(n)