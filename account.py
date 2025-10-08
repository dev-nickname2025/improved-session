from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid. Please Try again!")

class SavingAccount(Account):
    def deposit(self, amount):
        self.set_balance(self.get_balance() + amount)
        print(f"{self.owner} deposited {amount}. Total Balance : {self.get_balance()}")
    
    def withdraw(self, amount):
        if amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
            print(f"{self.owner} withdraw {amount}. Total Balance : {self.get_balance()}")
    
    def add_interest(self):
        interest = self.get_balance() * 0.5
        self.set_balance(self.get_balance() + interest)
        print(f"Intereste Added! Total amount: {self.get_balance()}")
    
class CurrentAccount(Account):
    def deposit(self, amount):
        self.set_balance(self.get_balance() + amount)
        print(f"{self.owner} deposited {amount}. Current Balance : {self.get_balance()}")
    
    def withdraw(self, amount):
        if amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
            print(f"{self.owner} withdraw {amount}. Remaining Balance : {self.get_balance()}")
        else:
            print("Insufficient Funds.")