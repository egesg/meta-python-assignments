# Import ABC and abstractmethod from the module abc (which stands for abstract base classes)
from abc import ABC, abstractmethod

# Class Bank
class Bank(ABC):
    """ An abstract bank class"""

    def basicinfo():
        print("This is a generic bank")
        return "Generic bank: 0"

    @abstractmethod
    def withdraw():
        pass

# Class Swiss
class Swiss(Bank):
    """ A specific type of bank than derives from class Bank"""

    def __init__(self, bal = 1000):
            self.bal = bal

    def basicinfo(self):
        print("This is the Swiss Bank")
        return "Swiss Bank: " + str(self.bal)
    
    def withdraw(self, amount):
        if self.bal >= amount:
            self.bal = self.bal - int(amount)
            print("Amount withdrawn: " + str(amount))
            print("New balance: " + str(self.bal))
        else:
            print("Insufficient fund")

        # do not forget to return 
        return self.bal