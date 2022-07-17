class Circle:

    __pi=0
    radius=0

    def __init__(self):
        self.__pi = 3.14
        self.radius = 5

    def calc_area(self):
        return self.__pi * self.radius ** 2

c1 = Circle()
print(c1.calc_area())
