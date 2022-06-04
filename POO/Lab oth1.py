class rectangle :
    def __init__(self,L,l):
        self.L =L
        self.l=l
    def surface(self):
        return self.l*self.L
    def perimetre(self):
        return (self.l+self.L)/2

class Parallelepipede(rectangle) :
    def __init__(self,L,l,h):
        self.h = h
        rectangle.__init__(self,L,l)
    def volume(self):
        return self.l*self.L*self.h

rectangle1=Parallelepipede(2,2,2)
print("la surface est : {}".format(rectangle1.surface()))
print("le volume est : {}".format(rectangle1.volume()))
print("Le perimetre est : {}".format(rectangle1.perimetre()))
