from math import atan, degrees
from matplotlib.pyplot import figure, plot, xlabel, ylabel, title, show
class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    def __str__(self):
        return 'Имя точки: {}. Координаты x: {}, y: {}'.format(self.name, self.x, self.y)

class Segment:
    def __init__(self, name, point1, point2):
        self.name = name
        self.point1 = point1
        self.point2 = point2

    def __str__(self):
        return 'Имя отрезка: {}. Координаты 1-ой точки - x: {}, y: {}. Координаты 2-ой точки - x: {}, y: {}'.format(self.name, p1.x, p1.y, p2.x, p2.y)
        
    def length(self):
        l = ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5
        print('Длина отрезка: ' + str(l))
    def angle(self):
        a = degrees(atan((p2.y - p1.y) / (p2.x - p1.x)))
        print('Угол к оси X: ' + str(a))
    def move(self, deltax1, deltay1, deltax2, deltay2):
        p1.x = p1.x + deltax1
        p2.x = p2.x + deltax2
        p1.y = p1.y + deltay1
        p2.y = p2.y + deltay2

p1 = Point('First', 0, 0)
#print(p1.name, p1.x, p1.y)
print(p1)

p2 = Point('Second', 4, 4)
#print(p2.name, p2.x, p2.y)
print(p2)

s1 = Segment('Segment 1', p1, p2)
#print(s1.name)
print(s1)

s1.length()
s1.angle()

s1.move(1, 2, 2, 3)

print(s1)
s1.length()
s1.angle()

x = (p1.x, p2.x)
y = (p1.y, p2.y)

figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
show()







