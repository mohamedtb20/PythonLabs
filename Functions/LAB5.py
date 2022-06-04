def somme(x, y, z):
    s = x + y + z
    return s
#we define a tuple
x = (1, 2, 2)
#somme(*x) will decompose all x element and consider them as an arguments
print("la somme de x :", somme(*x))
