import sys

class Bank(object):
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        return self.balance


    def withdraw(self,amount):
        if amount > self.balance:
            print('balance is less for withdrawal')
        else:
            self.balance-=amount
        return self.balance


name=input('Enter Name:')

b=Bank(name)

while(True):
    print('d -Deposit , w -withdraw , e -Exit')

    choice=input('Your choice :')

    if choice=='e' or choice=='E':
        sys.exit()

    amt=float(input('Enter amount: '))

    if choice=='d' or choice=='D':
        print('balance after deposit :',b.deposit(amt))
    
    elif choice=='w' or choice=='W':
        print('balance after withdrawal :',b.withdraw(amt))