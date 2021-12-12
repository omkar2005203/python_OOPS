import math
class Calculate:
    @staticmethod
    def calculate(x):
        return math.sqrt(x)

    
num = float(input('Enter a number :'))

res=Calculate.calculate(num)

print('square root of {} is {}'.format(num,res))