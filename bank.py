class Bank:
    def __init__(self,balance,owner,acc_no):
        self.balance=balance
        self.owner=owner
        self.acc_no=acc_no
    def details(self):
        return f"Dear {self.owner} of account number {self.acc_no} your account balance is {self.balance}."
    
    def deposit(self):
        return f"Dear {self.owner} thank you for using to deposit with us your balance is {self.balance}."

    def withdraw(self):
        return f"Dear {self.owner} you have withdrawnyour account balance is {self.balance}."

