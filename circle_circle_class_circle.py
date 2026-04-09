class Circle :
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius   
Circle1 = Circle(5)
print("Circle Area:", Circle1.area())
print("Circle Perimeter:", Circle1.perimeter())

