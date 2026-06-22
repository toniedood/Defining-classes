class BankAccount: 
    def __init__ (self, owner_name, account_number, balance):
        self.owner_name = owner_name
        self._account_number = account_number
        self.__balance = 0

    def deposit (self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposit successful. New balance: {self.__balance}"
        else:
            return "Deposit amount must be positive."
    
    def withdraw (self, amount):
        if amount > self.__balance:
            return "Insufficient funds."
        elif amount <=0:
            return "Withdrawal amount must be positive."
        else:
            self.__balance -= amount
            return f"Withdrawal successful. New balance: {self.__balance}"
        
    def get_balance (self):
        return f'Current balance is: {self.__balance}'
    
    def get_account_info (self):
        return f"Account number: {slef._account_number}, Owner: {self.owone_name}"


