# 4.17  Author: Adrian & June

# The program promps for six leading coefficients.
# Afterwards, the program outputs the x and y values needed to solve the 
# linear equation.

# The function solves for the x and y values:
def linear(coef) -> str:
    # Sets the x and y values to non-existent:
    xvalue = None
    yvalue = None
    # Solves for y:
    for x in range(-10, 11):
        for y in range(-10, 11):
            if ((x * (coef[0] - coef[3])) + (y * (coef[1] - coef[4]))) \
                == (coef[2] - coef[5]):
                yvalue = int(y)
                xvalue = int(x)
                break
    # Solves for x:
    if ((xvalue * coef[0] + yvalue * coef[1]) == coef[2]):
        pass
    else:
        xvalue = int(((coef[2] - yvalue * coef[1]) / coef[0]))
    if ((xvalue * coef[0] + yvalue * coef[1]) != coef[2]):
        xvalue = None
    # If there is no solution for the linear equation the program 
    # outputs that it does not exist:
    if (xvalue == None) or (yvalue == None):
        result = "There is no solution"
    else:
        result = f"x = {xvalue} , y = {yvalue}"
    return result

# Promps and stores the coefficients:
num_list = []
for i in range(6):
    integer = int(input())
    num_list.append(integer)

# Calls the function and outputs what it returns:
print(linear(num_list))