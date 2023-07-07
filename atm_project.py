class ATM:
    balance = 0

    def __init__(self, username, pwd):
        self.username = username
        self.pwd = pwd

    def checkBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount has been deposited. Current balance:", self.balance)

    def credit(self, amount):
        self.balance -= amount
        print("Amount has been credited. Current balance:", self.balance)

    def accountChecking(self):
        if self.username == "Marudhu" and self.pwd == 1234:
            while True:
                print("1) Check balance")
                print("2) Deposit")
                print("3) Credit")
                print("4) Exit")
                option = int(input("Enter your choice: "))

                if option == 1:
                    balance = self.checkBalance()
                    print("Your balance:", balance)
                elif option == 2:
                    amount = int(input("Enter your deposit amount: "))
                    self.deposit(amount)
                elif option == 3:
                    amount = int(input("Enter your credit amount: "))
                    if amount <= self.checkBalance():
                        self.credit(amount)
                    else:
                        print("Insufficient balance.")
                elif option == 4:
                    break
                else:
                    print("Invalid choice. Please try again.")

username = input("Enter your username:")
pwd = int(input("Enter your pwd:"))
# Create an instance of the ATM class
my_atm = ATM(username, pwd)

# Perform operations on the ATM
my_atm.accountChecking()

    



