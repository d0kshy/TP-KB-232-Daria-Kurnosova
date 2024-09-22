import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'topic_01')))

from task3 import findDelta

def findRoots(a, b, c, discriminant):
    a = float(a)
    b = float(b)
    c = float(c)

    if discriminant == 0:
        x1 = (-b+ discriminant**(1/2))/(2*a)
        print(f"Roots are the same:\nx1 = {x1}, x2 = {x1}.\n")
    
    elif discriminant > 0:
        x1 = (-b + discriminant**(1/2))/(2*a)
        x2 = (-b - discriminant**(1/2))/(2*a)
        print(f"Roots are: \nx1 = {x1}, x2 = {x2}.\n")
    
    elif discriminant < 0:
        print("Roots are not exist.\n")

a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")

print(f"\nYour equation is ({a})x^2 + ({b})x + ({c}) = 0.")
discriminant = findDelta(a, b, c)

print(f"The discriminant is {discriminant}.\n")
print(findRoots(a, b, c, discriminant))