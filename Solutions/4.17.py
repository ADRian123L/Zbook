# 4.17  Author: Adrian & June

def solver(coef) -> str:
    # SOLVING FOR Y:
    # Makes both Xs equal:
    if (coef[0] != coef[3]):
        mult = (coef[3] / coef[0])
        new_x1 = (coef[0] * mult)
        new_y1 = (coef[1] * mult)
        new_c = (coef[2] * mult)
    # Multiplies all other firsts coefficients by -1:
    new_y1 *= -1
    new_c *= -1
    
    # Adds both equations:
    constant = (new_c + coef[5])
    yvalue = (new_y1 + coef[4])

    # Getting y:
    y = (constant / yvalue)

    # SOLVING FOR X:
    x = ((coef[2] - (coef[1] * y)) / coef[0])

    return f"x = {int(x)}, y = {int(y)}"


# Promps and stores the coefficients:
num_list = []
for i in range(6):
    integer = int(input())
    num_list.append(integer)

print(solver(num_list))