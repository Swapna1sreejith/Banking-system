class Bank:
    def __init__(self, name):
        self.name = name
        self.account_holders = []

    def new_account(self, account):
        self.account_holders.append(account)


class Account:

    def __init__(self, number, user, balance):
        self.number = number
        self.user = user
        self.tot_balance = balance

    def deposit(self, amount):
        self.tot_balance += amount
        print("\nYour current balance is : ", self.tot_balance)

    def withdraw(self, amount):
        if self.tot_balance >= amount:
            self.tot_balance -= amount
            print("\nYour current balance is : ", self.tot_balance)
        else:
            print("Insufficient funds in your account")

    def user_details(self):
        print("\n -----> Details of the customer :  \n")
        print("\t Name : ", self.user)
        print("\t Account number : ", self.number)
        print("\t Your current balance : ", self.tot_balance)

    def disp_balance(self):
        if self.tot_balance <= 500:
            print("Always keep a minimum balance in your account to avoid penalty")
            print("\t Your current balance : ", self.tot_balance)
        else:
            print("\t Your current balance : ", self.tot_balance)

    def mod_account(self, amount):
        print("\nAccount Number : ", self.number)
        self.user = input("\nModify Account Holder Name, write the new name :")
        x = input("\n\tModify Balance : Y / N\t")
        if x.upper() == "Y":
            self.tot_balance += amount
        else:
            print("Balance is not modified")
        print("Account Number : ", self.number, "is modified to new credentials and balance")


def main():
    global acc_own
    bank_name = input("Enter bank name: ")
    bank = Bank(bank_name)
    print("Welcome to ", bank_name.upper(), "services")
    while True:
        print("""
        
        1. Create Account
        2. Login
        3. Exit
        
        """)
        choice = int(input("\n Enter your choice: "))
        if choice == 1:
            print("To create an account, please fill in the information below.")
            print()
            acc_num = input("Enter account number: ")
            acc_own = input("Enter account owner name: ")
            acc_bal = float(input("Enter opening balance: "))
            account = Account(acc_num, acc_own, acc_bal)
            bank.new_account(account)
            print("Account created successfully. Account holder name ", acc_own)
        elif choice == 2:
            print("To access your account, please enter your credentials below.")
            print()
            number = input("Enter account number: ")
            account = login(bank.account_holders, number)
            if account:
                print("Account of ", acc_own, "verification successful.Now you may use the following services")
                account.user_details()
                while True:
                    print()
                    print("""Choose an option:

                1. Withdraw
                2. Deposit
                3. Balance
                4. Modify account
                5. Exit
                
                                """)
                    acc_choice = int(input("1, 2, 3, 4, 5: "))

                    if acc_choice == 1:
                        print()
                        amount = float(input("Enter amount to withdraw: "))
                        account = login(bank.account_holders, number)
                        if account:
                            print("Withdrawal successful")
                            account.withdraw(amount)
                            print("The sum of Rs.", amount, " has been withdrawn from your account balance.")
                        else:
                            print("Account not found")
                    elif acc_choice == 2:
                        print()
                        amount = float(input("Enter amount to deposit: "))
                        account = login(bank.account_holders, number)
                        if account:
                            print("Deposit successful")
                            account.deposit(amount)
                            print("The sum of Rs.", amount, " has been deposited to your account balance.")
                        else:
                            print("Account not found")
                    elif acc_choice == 3:
                        account.disp_balance()
                    elif acc_choice == 4:
                        amount = float(input("Enter amount to be added to account balance: "))
                        account = login(bank.account_holders, number)
                        if account:
                            account.mod_account(amount)
                            account.user_details()
                        else:
                            print("Not modified")
                    elif acc_choice == 5:
                        print()
                        print("Thank you for visiting!")
                        exit()

            else:
                print("Account not found.Please enter a valid account")
        elif choice == 3:
            print("Thank you for using the ", bank_name, " Management System")
            break
        else:
            print("Invalid choice.Please enter a valid choice.")


def login(account_holders, number):
    for account in account_holders:
        if account.number == number:
            return account
    return None


main()