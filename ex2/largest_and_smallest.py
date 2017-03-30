# hadart_787, Hadar Treidel, 20325554


def largest_and_smallest(num1, num2, num3):
    """find the biggest and smallest numbers out of 3
       given numbers"""
    if num1 >= num2 and num1 >= num3:
        maximum = num1
    elif num2 >= num3:
        maximum = num2
    else:
        maximum = num3
    if num1 <= num2 and num1 <= num2:
        minimum = num1
    elif num2 <= num3:
        minimum = num2
    else:
        minimum = num3
    return maximum, minimum
