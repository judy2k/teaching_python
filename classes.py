



class Rectangle:
    corner = 90

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def perimeter(self):
        return self.w * 2 + self.h * 2

    def area(self):
        return self.w * self.h

    def angles(self):
        return self.corner * 4

    def __str__(self):
        return "Rectangle: " + str(self.w) + ", " + str(self.h)

    def __repr__(self):
        return "<Rectangle: " + str(self.w) + ", " + str(self.h) + ">"


r = Rectangle(10, 5)
a = Rectangle(12, 3)

print(r.w, r.h, r.angles())
print(a.w, a.h, a.angles())

r.corner = 5

print(r.w, r.h, r.angles())
print(a.w, a.h, a.angles())

