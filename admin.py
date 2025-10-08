class Admin:
    def approve_loan(self, account, amount):
        print(f"Admin approved loan for {amount} for {account.owner}")
        account.deposit(amount)
    
class AuditLog:
    def log_transaction(self, account, action, amount):
        print(f"Transaction: {action} {amount} for {account.owner}")

from account import SavingAccount

class EmployeeAccount(SavingAccount, Admin, AuditLog):
    pass