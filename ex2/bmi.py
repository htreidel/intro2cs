# hadart_787, Hadar Treidel, 20325554


def is_normal_bmi(weight, height):
    """calculates bmi and returns "True" if values are within
       range and "False" otherwise"""
    calculate_bmi = weight / (height**2)
    if calculate_bmi >= 18.5 and calculate_bmi <= 24.9:
        return True
    else:
        return False
