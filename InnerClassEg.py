class NonVeg:
    def __init__(self):
        self.chiken='biryani'
        self.gravy='handi'
        # self.st=self.Starters()

    def display(self):
        print('I want {} and {} in dinner'.format(self.chiken,self.gravy))

    

    class Starters:
        def __init__(self):
            self.desserts='ice-creams'
            self.appetizer='lemonade'

        def display(self):
            print('after dinner i want to have {} and {}'.format(self.desserts,self.appetizer))



p=NonVeg()
x=p.