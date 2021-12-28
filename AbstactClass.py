from abc import ABC,abstractmethod
import math
class Calculator(ABC): 
    @abstractmethod
    def calculate(self,x):
        pass



class Subcalone(Calculator):
    def calculate(self,x):
        return (x**2)



class Subcaltwo(Calculator):
    def calculate(self, x):
        return (x**3)


class Subcalthree(Calculator):
    def  calculate(self, x):
        return (math.sqrt(x))




ob1=Subcalone()
ob2=Subcaltwo()
ob3=Subcalthree()


print(ob1.calculate(4))
print(ob2.calculate(4))
print(ob3.calculate(4))