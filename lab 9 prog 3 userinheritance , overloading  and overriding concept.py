'''3.	create an abstract class shape and derive rectangle and circle from shape class. 
Implement abstract method of shape class in rectangle and  circle class. Shape class
 contains: origin (x,y) as data member Display() and area() as abstract methods.
 Circle contains : radious, Rectangle contains : length & width ( userinheritance 
 , overloading  and overriding concept.)'''


class Shape():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def display(self):
        pass
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.radius = r
    def display(self):
        print("Circle with center at ", '(',self.x,',', self.y,')')
    def area(self):
        return 3.14 * (self.radius ** 2)  #Area of circle = 3.14*r**2

class Rectangle(Shape):
    def __init__(self, x, y, l, w):
        super().__init__(x, y)
        self.length = l
        self.width = w
    def display(self):
        print("Rectangle with bottom-left corner at", '(',self.x,',', self.y,')')
    def area(self):
        return self.length * self.width  #Area of rectangle = length * breadth

c= Circle(0, 0, 10)
r= Rectangle(0, 0, 10, 20)
c.display()
print("Area of circle = ", c.area())
r.display()
print("Area of rectangle = ",r.area())
