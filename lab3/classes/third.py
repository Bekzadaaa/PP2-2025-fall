class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

length = float(input("Length:"))
width = float(input("width:"))
rectangle = Rectangle(length, width)
print("Rectangle area:", rectangle.area())