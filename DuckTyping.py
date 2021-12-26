class Duck:
    def talk(self):
        print("quack,quack")


class Human:
    def talk(self):
        print("Hi hello")

def call_it(obj):
    obj.talk()



x=Duck()
call_it(x)

y=Human()
call_it(y)