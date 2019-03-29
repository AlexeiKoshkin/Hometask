#В процессе
from math import atan, degrees
class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

class Segment:
    def __init__(self, name):
        self.name = name
        
    def length(self, point1, point2):
        l = ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5
        print(l)
    def angle(self, point1, point2):
        a = degrees(atan((p2.y - p1.y) / (p2.x - p1.x)))
        print(a)
    #def move(self, deltax, deltay):



p1 = Point('First', 0, 0)
print(p1.name, p1.x, p1.y)

p2 = Point('Second', 4, 4)
print(p2.name, p2.x, p2.y)

s1 = Segment('Segment 1')
print(s1.name)

s1.length(p1, p2)
s1.angle(p1, p2)







