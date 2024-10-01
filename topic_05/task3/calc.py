from operations import operation

answer = ''
print()
while answer != 'N':
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    symbol = input("Enter the action [+ addition, - subtraction, * multiplication, / dividing]: ")
    

    print(f"The result is equal to {operation(a, b, symbol)}")
    answer = input("Do you want to continue? [Y/N] ").upper()