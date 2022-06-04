# classes
class Point:
    def __init__(self, x, y):
        self.px = float(x)
        self.py = float(y)
class Segment:

    def __init__(self, x1, y1, x2, y2):
        self.orig = Point(x1, y1)
        self.extrem = Point(x2, y2)

    def __str__(self): #une foi dir x=segment(parametre) print(x) direct t affichilek hade return hit fonvtion tab3a l class
        #t9der dir fonction w t3ytlha lte7t w tdirha ghi t affichi
        return ("Segment : [({:g}, {:g}), ({:g}, {:g})]".format(self.orig.px, self.orig.py, self.extrem.px, self.extrem.py))
# Auto-test ---------------------------------------------------------
if __name__ == '__main__':
    s = Segment(1, 2, 3, 4)
    print(s)

#ou
class Point:
    def __init__(self, x, y):
        self.px = float(x)
        self.py = float(y)
class Segment:

    def __init__(self, x1,x2,y1,y2):
        Point.__init__(self,x1, y1)
        Point.__init__(self, x2, y2)
        self.orig = (x1, y1)
        self.extrem = (x2, y2)
    def __str__(self): #une foi dir x=segment(parametre) print(x) direct t affichilek hade return hit fonvtion tab3a l class
        #t9der dir fonction w t3ytlha lte7t w tdirha ghi t affichi
        return self.orig,self.extrem
# Auto-test ---------------------------------------------------------
if __name__ == '__main__':
    s = Segment(1, 2, 3, 4)
    print(s)