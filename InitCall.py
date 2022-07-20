class Person:
    def __init__(self,fname,lname):
        print("parent initializer called")
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)

    def display(self):
        print("method from parent class")

    
class Lawyer(Person):
    def __init__(self, fname, lname,casetype):
        print("child initiliazer called ")
        Person.__init__(self,fname,lname)
        self.casetype=casetype

    def printinfo(self):
        print(self.firstname,self.lastname)
    
    def display(self):
        print("method from child class")

obj = Lawyer('Omkar','Rane','civil')
obj.printinfo()
obj.display()
print(obj.casetype)