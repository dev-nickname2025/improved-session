from account import SavingAccount, CurrentAccount
from admin import EmployeeAccount

def main():
    print("--- Day 15 Bank Management System ---\n")

    sa = SavingAccount("John", 1000)
    sa.deposit(500)
    sa.add_interest()
    sa.withdraw(200)

    print("\n--- Current Account ---")
    ca = CurrentAccount("Mg Mg", 2000)
    ca.deposit(1000)
    ca.withdraw(500)

    print("\n--- Employee Account (Multiple Inheritance) ---")
    ea = EmployeeAccount("Su Su", 1500)
    ea.deposit(300)
    ea.add_interest()
    ea.approve_loan(ea, 2000)
    ea.log_transaction(ea, "Deposit", 300)

if __name__ == "__main__":
    main()