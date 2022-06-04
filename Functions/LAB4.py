def somme(*x):
    s = 0
    for i in x:
        s = s + i
    return s

y=(1, 2, 3, 4)
print('sum of x=(1,2,3,4) : ', somme(*y))
