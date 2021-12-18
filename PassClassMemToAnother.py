class Emp:
    def __init__(self,id,name,sal):
        self.name=name
        self.id=id
        self.sal=sal

    
    def display(self):
        print('his name is {} and his id is {} and sal is {}'.format(self.name,self.id,self.sal))

    

class Myclass:

    @staticmethod
    def mymethod(e):
        e.sal+=1000
        e.display()



e=Emp(1,'Nikhil',2000)

Myclass.mymethod(e)
