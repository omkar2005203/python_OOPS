class Test:
    numOne=0
    numTwo=0

    def __init__(self,x,y):
        self.numOne = x
        self.numTwo = y


    def equals(self,obj):
        if(obj.numTwo == self.numTwo):
            return True
        else:
            return False

    
obj1 = Test(10,20)
obj2 = Test(10,30)

print(obj1.equals(obj2))