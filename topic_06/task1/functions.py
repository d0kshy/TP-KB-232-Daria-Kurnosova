def addition(a, b):
    try:
        sum = int(a) + int(b)
        return sum
    except ValueError:
        print("Error: Please, enter a valid number!")
        return None

def subtraction(a, b):
    try:
        difference = int(a) - int(b)
        return difference
    except ValueError:
        print("Error: Please, enter a valid number!")
        return None

def multiplying(a, b):
    try:
        product = int(a) * int(b)
        return product
    except ValueError:
        print("Error: Please, enter a valid number!")
        return None


def dividing(a, b):
    try:
        quot = int(a) / int(b)
        return quot
    except ZeroDivisionError:
        print("Error: You can/'t divide numbers by zero! Please enter a valid number!")
        return None  