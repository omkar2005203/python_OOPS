
class Test:
    def func(self):
        print("this is func")

    def monk(self):
        print("test patch !")



class newTest:
    def my_func(self):
        print("This is patched !")


    def test_my(self):
        print("This is !")



Test.func = newTest.my_func

newTest.test_my = Test.monk



ob = Test()

ob1 = newTest()

ob.func()

ob1.test_my()