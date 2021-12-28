## multi-level inheritance example

class A:
    name=' '
    age=0


class B(A):
    height=' '

class C(B):
    weight=' '

    def Read(self):
        print('Enter following data:')

        self.name=input('Enter your name :')
        self.age=int(input('Enter your age :'))
        self.weight=float(input('Enter your weight :'))
        self.height=float(input('Enter height :'))


    def display_data(self):
        print('Name: ',self.name)
        print('Age :',self.age)
        print('Weight :',self.weight)
        print('Height :',self.height)





c=C()
c.Read()
c.display_data()

