import math
class Square:
    def __init__(self,x):
        self.x=x

    def area(self):
        print('square area is {}'.format(self.x*self.x))

class Circle(Square):
    def __init__(self,x):
        super().__init__(x)


    def area(self):
        super().area()
        print('circle area is {}'.format(math.pi*self.x*self.x))



c=Circle(4)
c.area()