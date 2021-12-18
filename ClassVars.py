class Student():
    #class variable/static vars
    x=10

    # class method to modify x
    @classmethod
    def modify(cls):
        cls.x+=1

s=Student()
print(s.x)
print(Student.x)
s.modify()
print(s.x)
print(Student.x)