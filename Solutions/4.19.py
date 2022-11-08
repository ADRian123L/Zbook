# -*- coding: utf-8 -*-
# 4.19.py  Author: Adrian

# The program prompts for three integers and outputs a drawing of a 
#  triangle.

# Variables:
run = False
character = "*"

# Prompts for the integers:
try:
    height = int(input())
    width = int(input())
    arrow = int(input())
except:
    height = 6
    width = 4
    arrow = 4

# Validates the arrow input:
if (arrow <= width):
    run = True

while run:
    arrow = int(input())
    if not (arrow <= width):
        run = False

# Draws the rectangle;
for i in range(1, height + 1):
    line = character * width
    print(line)

# Draws the arrow:
for i in range(1 ,arrow + 1):
    line = character * arrow
    arrow -= 1
    print(line)