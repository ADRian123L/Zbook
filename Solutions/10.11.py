# -*- coding: utf-8 -*-
# 10.11.py  Author: Adrian

# The program creates a car class for storing its attributes.

class Car:
    """An object for calculating the present value of a car."""
    def __init__(self) -> None:
        # The two attributes that the user will change:
        self.purchase_price = 0
        self.model_year = 0
        # The attribute that the calc method calculates:
        self.current_price = 0
        return None

    def calc_current_value(self, current_year : int) -> None:
        '''Changes the value of current_price depending on the year after
            purchase.'''
        depreciation  = 0.15
        car_age = current_year - self.model_year
        self.current_price = round(self.purchase_price * \
                            ((1 - depreciation) ** car_age))
        return None

    def print_info(self) -> None:
        '''Prints the information stored.'''
        head = "Car's information:\n"
        price_line = f"{'':>2}Model year: {self.model_year}\n"
        purchase_line = f"{'':>2}Purchase price: ${self.purchase_price}\n"
        current_line = f"{'':<2}Current value: ${self.current_price}"
        format = head + price_line + purchase_line + current_line
        print(format)
        return None

if __name__ == "__main__":
    # Prompts for the car's information: 
    year = int(input())
    price = int(input())
    current_year = int(input())

    # Applies the attributes:
    my_car = Car()
    my_car.purchase_price = price
    my_car.model_year = year
    my_car.calc_current_value(current_year)
    my_car.print_info()