class Circle:
    pi = 3.14
    def __init__(self, radius, cirfer, area):
        self.radius = radius
        self.cirfer = cirfer
        self.area = area

    def Accept(self):
        self.radius = int(input("Enter radius"))

    def CalculateArea(self):
        self.area = self.radius * self.radius

    def CalculateCircumference(self):
        self.cirfer = 2 * Circle.pi * self.radius

    def Display(self):
        print("Radius is: ",self.radius)
        print("Circumference is: ",self.cirfer)
        print("Area is: ",self.area)

def main():
    obj1 = Circle(0.0, 0.0, 0.0)
    obj2 = Circle(0.0, 0.0, 0.0)

    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    obj2.Accept()
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()

if __name__ == '__main__':
    main()