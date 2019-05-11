class Point:
    def __init__(self,x,y):
        self.xs = x
        self.ys = y
    def __str__(self):
        return ('Point({},{})'.format(self.xs,self.ys))
    def __add__(self, other):
        return Point(self.xs + other.xs,self.ys + other.ys)
    def __sub__(self, other):
        return Point(self.xs - other.xs,self.ys - other.ys)
    def distance(self, other):
        return (pow(((self.xs-other.xs)**2+(self.ys-other.ys)**2),0.5))

p1 = Point (1,2)
p2 = Point (3,4)
p3 = p1+p2

print ('p1 = ',p1,' p2 = ',p2)
print ('p3 = ',p3)
print ('p1 + p2 = ',p1+p2)
print ('p1 - p2 = ',p1-p2)
print ('distance p1,p2= ',p1.distance(p2))

