## program 1
class Student:
    def __init__(self):
        # instance variable
        self.name='Omkar'
        self.age=23
        self.marks=900
    
    # instance method
    def talk(self):
        print('my name is ',self.name)
        print('my age is ',self.age)
        print('my marks are ',self.marks)


s1=Student()
s1.talk()

print(id(s1))