"""
半径1の円
cricle1 = Circle(radius=1)
print(circle.area())
print(circle.perimeter())
"""
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f'{(self.radius ** 2) * math.pi:.2f}'

    def perimeter(self):
        return f'{self.radius * 2 * math.pi:.2f}'

circle1 = Circle(radius=1)
print('circle1')
print(circle1.area())
print(circle1.perimeter())


circle3 = Circle(radius=3)
print('circle3')
print(circle3.area())
print(circle3.perimeter())