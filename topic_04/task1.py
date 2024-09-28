def calculator(a, b, symb):
    try:
        match symb:
            case '+':
                sum = int(a) + int(b)
                print(f"The sum is {sum}.")
            
            case '-':
                diff = int(a) - int(b)
                print(f"The difference is {diff}.")

            case '*':
                prod = int(a) * int(b)
                print(f"The product is {prod}.")

            case '/':
                quo = int(a) / int(b)
                print(f"The quotient is {quo}.")

            case '**':
                pwr = int(a) ** int(b)
                print(f"The power is {pwr}.")
                
    except ValueError:
         print("Error: Please enter valid numbers!")

a = input("Enter the first number: ")
b = input("Enter the second number: ")
s = input("Enter the action: ")

calculator(a, b, s) 