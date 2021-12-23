class InstanceCount:
    def __init__(self):
        self.n=0
        
    def counter(self):
        self.n+=1
        print('instance count :',self.n)

    

i=InstanceCount()
j=InstanceCount()
j.counter()