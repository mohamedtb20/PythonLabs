# the cube of a variable
def cube(x):
    return (x ** 3)


# we import pi=3.14 to use on the volume
from math import pi


# we use a function that calcul the volume of a sphere
def volumeS(r):
    return ((4 * pi * cube(r)) / 3)


r = float(input('give the radius: '))
print("the volume of the sphere is = ", volumeS(r))
