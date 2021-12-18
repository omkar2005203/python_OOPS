class Person:
    def __init__(self):
        self.name='tom'
        ## creating of object of inner class
        self.db=self.Dob()


    def display(self):
        print('Name=',self.name)


    ## inner class
    class Dob:
        def __init__(self):
            self.dd=19
            self.mm=12
            self.yy=2021

        def display(self):
            print('Dob={}/{}/{}'.format(self.dd,self.mm,self.yy))

p=Person()
x=p.db
x.display()
## method 2
# p=Person().Dob()
print(x.dd)
p.display()