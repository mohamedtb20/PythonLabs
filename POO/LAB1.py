class vect2d :
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        self.other=other
        return (self.x + other.x ,self.y + other.y)
    def __str__(self):
        return "vecteur({:g}, {:g})" .format(self.x, self.y)

vecteur1=vect2d(5,5)
vecteur2=vect2d(2,3)
somme=vect2d.__add__(vecteur2,vecteur1)
print(vecteur1)
print(vecteur2)
print(somme)


