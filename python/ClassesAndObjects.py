# creating a class
class Employee:
    def __init__(self, name):
        self.name = name  # name is a data field also known as instance field

    def who_am_i(self):
        return "I am " + self.name


p = Employee('geek')
print(p.who_am_i())
print(p.name)
p.name='geeknarrator'
print(p.name)

#Hiding data outside the class (private from java)

class BankAccount:
    def __init__(self, name, money):
        self.__name = name   # using __ before the variable name makes it private (class accessible only)
        self.__money = money

    def deposit(self, money):
        self.__money += money

    def withdraw(self, money):
        if money > self.__money :
            print("Insufficient balance")
        else:
            self.__money -= money
            print("Transaction complete. Available balance", self.__money)

    def check_balance(self):
        print("Your balance is : ", self.__money)

b = BankAccount("geeknarrator", 100)
b.deposit(100)
b.withdraw(100)
b.check_balance()
b.withdraw(150)
