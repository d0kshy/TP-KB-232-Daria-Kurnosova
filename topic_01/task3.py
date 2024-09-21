def findDelta(a, b, c):
    delta = b**2 - 4*a*c
    return delta

discriminant = findDelta(4,4,1)
print(f"The discriminant is {discriminant}.")