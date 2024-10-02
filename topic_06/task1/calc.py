from operations import operation
import logging
logging.basicConfig(filename = 'topic_06/task1/task1.log', 
                    level = logging.INFO, 
                    format = '%(asctime)s - %(levelname)s - %(message)s')

answer = ''
n = 1
print()

while answer != 'N':
    print()
    print(f"Action №{n}")

    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    symbol = input("Enter the action [+ addition, - subtraction, * multiplication, / dividing]: ")
    
    result = operation(a, b, symbol)

    print(f"The result is equal to {result}")
    logging.info(f"Action #{n}: {a} {symbol} {b} = {result}")

    answer = input("Do you want to continue? [Y/N] ").upper()
    n += 1