class rectangle :
    def __init__(self,L,l):
        self.longeure=L
        self.largeur=l
        self.nom='rectangle'
    def __str__(self):
        return ('le {} a : la longueur est : {} , la largeur est : {}'.format(self.nom,self.largeur,self.longeure))

    def multiplication(self):
        return (self.largeur*self.longeure)
class carre(rectangle) :
    def __init__(self,L,l):
        self.nom='carre'
        rectangle.__init__(self,L,l)
notrerectangle = rectangle(5,2)
notrecarre=carre(4,4)
surfaceR=rectangle.multiplication(notrerectangle)
surfaceC=rectangle.multiplication(notrecarre)
print(notrerectangle)
print(surfaceR)
print(notrecarre)
print(surfaceC)

