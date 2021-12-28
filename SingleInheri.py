#  single inheritance example
class A:
    i=0
    j=0

    def showij(self):
        print(' i ',self.i,'and  j',self.j)


class B(A):
    k=0

    def showijk(self):
        print(' i ',self.i,' and  j ',self.j,' and k ',self.k)




obj1=B()

obj1.i=200
obj1.j=300

obj1.showij()

obj1.k=400
obj1.showijk()
