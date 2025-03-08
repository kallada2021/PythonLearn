class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance
    
    def get_balance(self):
        return f"AccountNumber: {self.account_number} has a balance of ${self.__balance}"
    
    def deposit(self,amount):
        if self.__balance >= 0:
            self.__balance += amount
        return self.__balance
    
    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            return self.__balance
        else:
            return f"Insufficient funds"
        
    

bankacct = BankAccount(12345678, 5000)
print(bankacct.get_balance())
print(bankacct.deposit(100))
print(bankacct.withdraw(5500))