class Student:
    # def __init__(self,n='',m=0):
    #     self.name=n
    #     self.marks=m
    
    # def display(self):
    #     print('Hi ',self.name)
    #     print('Your marks ',self.marks)

    ## mutator method

    def setName(self,name):
        self.name=name
    
    def setMarks(self,marks):
        self.marks=marks

    ## getter methods or accessor methods

    def getName(self):
        return self.name

    def getMarks(self):
        return self.marks
        
    def calculate(self):
        if self.marks>600:
            print('first class')
        elif self.marks>=500:
            print('you got second')
        elif self.marks>=350:
            print('you got third grade')
        else:
            print('you failed try again')

n=int(input('How many students ?'))
i=0
while(i<n):
    name=input('Enter name:')
    marks=int(input('Enter marks :'))

    s=Student()
    s.setName(name)
    s.setMarks(marks)
    print('Hi ',s.getName())
    print('Your marks ',s.getMarks())
    s.calculate()
    i+=1
    print('----------------------------------------------')