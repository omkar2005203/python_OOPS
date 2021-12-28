class Duck:
    def talk(self):
        print('quack quack')

class Human:
    def talk(self):
        print('Hi hello !')


class Dog:
    def bark(self):
        print('bow bow')


def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()

    elif hasattr(obj,'bark'):
        obj.bark()

    else:
        print('object not found!')


x=Duck()
call_talk(x)

h=Human()
call_talk(h)

d=Dog()
call_talk(d)