answer = ' '
while answer != 'No':
    a = input("\nEnter the first number: ")
    b = input("Enter the second number: ")
    symb = input("Enter the action: ")

    if symb == '+':
        sum = int(a) + int(b)
        print(f"The sum is {sum}.")
    
    elif symb == '-':
        diff = int(a) - int(b)
        print(f"The difference is {diff}.")

    elif symb == '*':
        prod = int(a) * int(b)
        print(f"The product is {prod}.")

    elif symb == '/':
        quo = int(a) / int(b)
        print(f"The quotient is {quo}.")

    elif symb == '**':
        pwr = int(a) ** int(b)
        print(f"The power is {pwr}.")

    answer = input("Do you want to continue? (Yes/No)\nAnswer: ")