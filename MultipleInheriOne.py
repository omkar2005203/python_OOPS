class Father(object):
    pass
    # def __init__(self):
    #     self.a='a'
    #     print(self.a)

class Mother(object):
    # pass
    def __init__(self):
        self.b='b'
        print(self.b)


class Son(Mother,Father):
    def __init__(self):
        self.c='c'
        print(self.c)
        super().__init__()
    

s=Son()
