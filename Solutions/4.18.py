# -*- coding: utf-8 -*-
# 4.18.py  Author: Adrian

# The program outputs a right triangle made up of special symbols.

# Prompts:
try:
    character = str(input("Enter a character:\n"))
    height = int(input("Enter triangle height:\n"))
except:
    # Variables:
    character = "%"
    height = 5

# Add empty space to character:
character = character + " "

# Prints the triangle:
print()
for i in range(1, height + 1):
    line = character * i
    print(line)