from Teacher import Teacher

class Student(Teacher):
    def setmarks(self,marks):
        self.marks=marks

    def getmarks(self):
        return self.marks



s1=Student()

s1.setname('omkar')
print(s1.getname())