# hadart_787, Hadar Treidel, 20325554
def quadratic_equation(a, b, c):
    """takes coefficients of a quadric equation of the
       sort of a*(x**2) + b*x + c = 0 and returns solutions for x"""
    if b**2 - 4 * a * c > 0:
        root1 = (-b + (b**2 - 4 * a * c)**0.5) / (2 * a)
        root2 = (-b - (b**2 - 4 * a * c)**0.5) / (2 * a)
    elif b**2 - 4 * a * c == 0:
        root1 = -b / (2 * a)
        root2 = None
    else:
        root1 = None
        root2 = None
    return root1, root2


def quadratic_equation_user_input():
    """recieves coefficients for quadric equation from user in format
       of: a b c and prints solutions for x"""
    string_coefficients = input("Insert coefficients a, b, and c: ", )
    coefficients = string_coefficients.split()
    root1, root2 = quadratic_equation(float(coefficients[0]),
                   float(coefficients[1]), float(coefficients[2]))
    if root2 and root2 != 0:
        print("The equation has 2 solutions:", root1, "and", root2)
    elif root1 and root1 != 0:
        print("The equation has 1 solution:", root1)
    else:
        print("The equation has no solutions")
