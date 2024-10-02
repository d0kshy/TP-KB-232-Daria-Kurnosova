import functions

def operation(a, b, symb):
    if symb == '+':
        return functions.addition(a, b)
    elif symb == '-':
        return functions.subtraction(a, b)
    elif symb == '*':
        return functions.multiplying(a, b)
    elif symb == '/':
        return functions.dividing(a, b)