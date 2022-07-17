class Person:
    def __init__(self,fname,lname):
        print("Constructor called from parent class")
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)


class Lawyer(Person):
    def __init__(self,fname,lname):
        print("Constructor called from child class")
        self.firstname=fname
        self.lastname=lname
    def printinfo(self):
        print(self.firstname,self.lastname)



happy_person = Lawyer("Tom","Cruise")
happy_person.printinfo()
