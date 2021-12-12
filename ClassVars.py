class Student():
    #class variable/static vars
    x=10

    @classmethod
    def modify(cls):
        cls.x+=1

s=Student()
print(s.x)
print(Student.x)
s.modify()
print(s.x)