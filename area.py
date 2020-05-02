import math

# Inputs

# obtaining length and width as input
length = input(4000)
width = input(5000)

# converting length/width to int
length = int(length)
width = int(width)

# calculate perimeter
perimeter = length * 2 + width * 2

# convert to string
perimeter = str(perimeter)

# concatenation
print( perimeter + feet)

# using sqrt from math library

square = input(43560)
square = float(square)

root = math.sqrt(square)

print(root)


#boolean operators
boo11 = False
boo12 = True
boo13 = False

# Three boolean Operators: and or not
# and operator: returns true if and only if both sides of the "and" are true
andTest = True and boo12
print(andTest)

# OR operator: returns true if one or both sides of it are true
orTest = boo11 or boo12
print(orTest)

# NOT operator: flips true to false, and false to true
notTest = not boo13

# Combining boolean operators

# order of boolean operations: NOT first, AND second, OR last
orderTest = not boo11 or boo13 and boo12
print(orderTest)