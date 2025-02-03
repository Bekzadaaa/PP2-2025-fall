import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
    
x1 = float(input("Enter x coordinate for point 1: "))
y1 = float(input("Enter y coordinate for point 1: "))
x2 = float(input("Enter x coordinate for point 2: "))
y2 = float(input("Enter y coordinate for point 2: "))

p1 = Point(x1, y1)
p2 = Point(x2, y2)

p1.show()

dx = float(input("Enter how much to move point 1 along the x-axis: "))
dy = float(input("Enter how much to move point 1 along the y-axis: "))
p1.move(dx, dy)

p1.show()

distance = p1.dist(p2)
print(f"Distance between points: {distance}")
