# hadart_787, Hadar Treidel, 20325554


def calculate_mathematical_expression(number1, number2, arithmatic_operator):
    """calculates one of four basic arithmetic actions '+','-','*','/'
       between two numbers"""
    num1 = float(number1)
    num2 = float(number2)
    if arithmatic_operator == '+':
        calculation = num1 + num2
    elif arithmatic_operator == '-':
        calculation = num1 - num2
    elif arithmatic_operator == '*':
        calculation = num1 * num2
    elif arithmatic_operator == '/':
        if num2 == 0:
            calculation = None
            return calculation
        calculation = num1 / num2
    else:
        calculation = None
    return calculation


def calculate_from_string(text_messege):
    """recieves string of arithmatic operator and returns calculation"""
    split_to_parts = text_messege.split(' ')
    num1 = split_to_parts[0]
    num2 = split_to_parts[2]
    arithmatic_operator = split_to_parts[1]
    return calculate_mathematical_expression(num1, num2, arithmatic_operator)
