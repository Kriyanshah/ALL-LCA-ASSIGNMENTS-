import math
x  = float(input("Enter the first side:"))
y  = float(input("Enter the second side:"))
z = float(input("Enter the third and the longest side:"))
def triangle(x,y,z):
    sides = [x,y,z]
    sides.sort()
    x= sides[0]
    y= sides[1]
    z= sides[2]
    if z*z == x*x + y*y:
        return True 
    else:
        return False
if triangle(x,y,z):
    print("Right angle triangle")
else:
    print("Not a right angle triangle")
