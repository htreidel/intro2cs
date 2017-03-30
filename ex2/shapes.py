# hadart_787, Hadar Treidel, 20325554
import math


def calculate_circle_area(radius):
    """calculates circle area with given radius"""
    area = math.pi * (radius**2)
    return area


def calculate_square_area(side1, side2):
    """calculates square area with given sides"""
    area = side1 * side2
    return area


def calculate_trapezoid_area(base1, base2, height):
    """calculates trapezoid area with given bases and height"""
    area = (base1 + base2) / 2 * height
    return area


def shape_area():
    """calculates area of a given shape: circle, rectangle or trapezoid"""
    shape_select = float(
        input("Choose shape (1=circle, 2=rectangle, 3=trapezoid): ", ))
    if shape_select != 1 and shape_select != 2 and shape_select != 3:
        return None
    elif shape_select == 1:
        return calculate_circle_area(float(input()))
    elif shape_select == 2:
        return calculate_square_area(float(input()), float(input()))
    else:
        return calculate_trapezoid_area(float(input()),
                                        float(input()), float(input()))
