class Student:
    def __init__(self,n='.',m=0):
        self.name=n
        self.marks=m

    def data(self):
        print('my name is ',self.name)
        print('my marks are ',self.marks)


s=Student()
s.data()

s1=Student('Omkar',100)
s1.data()