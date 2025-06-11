class Circle:
    
    def __init__(self, radius: float):
        self._radius = radius
        
    @property
    def area(self) -> float:
        """Calculate the area of the circle."""
        return 3.14159 * (self._radius ** 2)
    
    @property
    def radius(self) -> float:
        """Get the radius of the circle."""
        return self._radius
    
    @radius.setter
    def radius(self, value: float):
        """Set the radius of the circle."""
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = value
    
circle = Circle(5)
print(circle.area)  # Output: 78.53975
circle.radius = 10
print(circle.area)  # Output: 314.159
print(circle.radius) # Output: 10

