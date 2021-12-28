class Pages:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        return self.pages+other.pages


class Book:
    def __init__(self,pages):
        self.pages=pages



b1=Pages(25)
b2=Book(25)

print(b1+b2)
