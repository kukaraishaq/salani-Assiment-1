import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


# Example usage:
circle1 = Circle(5)  # Circle with radius 5
print("Radius:", circle1.radius)
print("Area:", circle1.area())
print("Perimeter:", circle1.perimeter())
