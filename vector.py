import random

class Vector():
    """Class representing a vector in cartesian coordinates"""
    def random(str='XYZ'):
        """Generates a random unit vector in a given space"""
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1*((1-(x**2))**2),((1-(x**2))**2))
        z = (1 - (x**2) - (y**2))**0.5
        return Vector(x, y, z)
    def zero():
        """Generates a zero vector"""
        return Vector(0, 0, 0)
    def __init__(self, x=0, y=0, z=0):
        # magnitude components
        self.x = x
        self.y = y
        self.z = z
        self.get_length()
        self.get_unit_vector()
    def get_length(self):
        """calculate and return length"""
        self.length = ((self.x**2)+(self.y**2)+(self.z**2))**0.5
        return self.length
    def get_unit_vector(self):
        """returns and saves a unit vector representation of the vector"""
        if self.is_unit():
            #prevents infinite recursion during initialization
            self.x_unit = self.x
            self.y_unit = self.y
            self.z_unit = self.z
            self.unit_vector = self
        elif self.is_zero():
            #prevents divide by zero errors
            self.x_unit = 0
            self.y_unit = 0
            self.z_unit = 0
            self.unit_vector = self
        else:
            self.x_unit = self.x/self.length
            self.y_unit = self.y/self.length
            self.z_unit = self.z/self.length
            self.unit_vector = Vector(self.x_unit, self.y_unit, self.z_unit)
        return self.unit_vector
    def invert(self):
        """reverses the direction of the vector"""
        self = self * -1
        return self
    def copy(self):
        return Vector(self.x, self.y, self.z)
    def is_zero(self):
        return self.length == 0
    def is_unit(self):
        return self.length == 1
    def add(self, other):
        """
        adds vector components
        usage: vec_1.add(vec_2)
        """
        if isinstance(other, (int, float)):
            self.x = self.x + other
            self.y = self.y + other
            self.z = self.z + other
        elif isinstance(other, Vector):
            self.x = self.x + other.x
            self.y = self.y + other.y
            self.z = self.z + other.z
        self.recalculate()
        return self
    def recalculate(self):
        """recalculates length and updates unit vector when vector is changed"""
        self.get_length()
        self.get_unit_vector()
        return self
    def clear(self):
        """resets vector to a zero vector"""
        self.x = 0
        self.y = 0
        self.z = 0
        self.recalculate()
        return self
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x + other,
                          self.y + other,
                          self.z + other)
        elif isinstance(other, Vector):
            return Vector(self.x + other.x,
                          self.y + other.y,
                          self.z + other.z)
    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x + other,
                          self.y + other,
                          self.z + other)
        elif isinstance(other, Vector):
            return Vector(self.x + other.x,
                          self.y + other.y,
                          self.z + other.z)
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x - other,
                          self.y - other,
                          self.z - other)
        elif isinstance(other, Vector):
            return Vector(self.x - other.x,
                          self.y - other.y,
                          self.z - other.z)
    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Vector(other - self.x,
                          other - self.y,
                          other - self.z)
        elif isinstance(other, Vector):
            return Vector(other.x - self.x,
                          other.y - self.y,
                          other.z - self.z)
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other,
                          self.y * other,
                          self.z * other)
        elif isinstance(other, Vector):
            return Vector(self.x * other.x,
                          self.y * other.y,
                          self.z * other.z)
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(other * self.x,
                          other * self.y,
                          other * self.z)
        elif isinstance(other, Vector):
            return Vector(other.x * self.x,
                          other.y * self.y,
                          other.z * self.z)
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x / other,
                          self.y / other,
                          self.z / other)
        elif isinstance(other, Vector):
            return Vector(self.x / other.x,
                          self.y / other.y,
                          self.z / other.z)
    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(other / self.x,
                          other / self.y,
                          other / self.z)
        elif isinstance(other, Vector):
            return Vector(other.x / self.x,
                          other.y / self.y,
                          other.z / self.z)
    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x // other,
                          self.y // other,
                          self.z // other)
        elif isinstance(other, Vector):
            return Vector(self.x // other.x,
                          self.y // other.y,
                          self.z // other.z)
    def __rfloordiv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(other // self.x,
                          other // self.y,
                          other // self.z)
        elif isinstance(other, Vector):
            return Vector(other.x // self.x,
                          other.y // self.y,
                          other.z // self.z)
    def __str__(self):
        return "<{}, {}, {}>".format(self.x, self.y, self.z)

def main():
    i = Vector(1, 0, 0)
    j = Vector(0, 1, 0)
    k = Vector(0, 0, 1)

main()
i = Vector(1, 0, 0)
j = Vector(0, 1, 0)
k = Vector(0, 0, 1)

if __name__ == '__main__':
    main()
