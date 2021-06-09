from datetime import datetime
# class Bank:
#     def __init__(self,balance,owner,acc_no):
#         self.balance=balance
#         self.owner=owner
#         self.acc_no=acc_no
#     def details(self):
#         return f"Dear {self.owner} of account number {self.acc_no} your account balance is {self.balance}."
    
#     def deposit(self):
#         return f"Dear {self.owner} thank you for using to deposit with us your balance is {self.balance}."

#     def withdraw(self):
#         return f"Dear {self.owner} you have withdrawnyour account balance is {self.balance}."


class Account:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.balance=0
        self.tran__fee=50
        self.loan=0
        self.loan_fees=0.05
        self.loan_limit=50000
        self.transactions=[]

    def deposit(self,amount):
        if amount<=0:
            return "Please deposit a valid amount"
        else:
           self.balance+=amount
           transaction={"amount":amount,"balance":self.balance,"narration":"You deposited","time":datetime.now()}
           self.transactions.append(transaction)
           return f"Hello {self.name}, you have deposited {amount} your new balance is {self.balance}"
    def withdraw(self,amount):
        transaction=amount+self.tran__fee
        if amount < 0:
            return "Cannot withdraw amount if it is zero or less"
        elif self.balance < transaction:
            return "cannot withdraw if balance is less than the amount plus the transaction fee"
        else:
            self.balance-=transaction
            transaction={"amount":amount,"balance":self.balance,"narration":"You withdraw","time":datetime.now()}
            self.transactions.append(transaction)
            return f"Hello {self.name} you have withdrawn {amount} successfully your balance is {self.balance}"
    def borrow(self,amount):  
        if amount < 0:
            return "You are not eligible for a loan"
        elif self.loan > 0:
            return "You cannot borrow a loan"  
        elif self.loan_limit < amount:
            return "Loan request greater than loan limit"
        else:
            loan_interest=self.loan_fees*amount  
            self.balance+=amount
            self.loan+=amount
            transaction={"amount":amount,"balance":self.balance,"narration":"You borrowed","time":datetime.now()}
            self.transactions.append(transaction)
            return f"Good morning {self.name} you have borrowed {amount} your new balance is {self.balance} to be paid in 90 days."

    def get_statement(self):
        for transaction in self.transactions:
            amount=transaction["amount"]
            narration=transaction["narration"]
            balance=transaction["balance"]
            time=transaction["time"]
            date=time.strftime('%D')
            print(f"Hello {self.name} on {date}  {narration} {amount} your balance is {balance}")

    def repay(self,amount):
        if amount < 0:
            return "You have to repay your loan"
        elif amount>self.loan:
            rem=amount-self.loan
            self.balance+=rem
            transaction={"amount":amount,"balance":self.balance,"narration":"You repaid","time":datetime.now()}
            self.transactions.append(transaction)
            return "You have paid your loan"
        else:
            self.loan-amount
            transaction={"amount":amount,"balance":self.balance,"narration":"You repaid","time":datetime.now()}
            self.transactions.append(transaction)

        




















