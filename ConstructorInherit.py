class Father:
    def __init__(self):
        self.property=8000000

    def display(self):
        print(self.property)


class Son(Father):
    pass


s=Son()

s.display()