#1.	Write a python class named circle constructed by a radius and two methods which will compute area and perimeter.

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print('area : ',3.14*(self.radius)**2)
    def perimeter(self):
        print('perimeter : ',2*3.14*self.radius)
r=int(input('enter the radius : '))
c=Circle(r)
c.area()
c.perimeter()            
