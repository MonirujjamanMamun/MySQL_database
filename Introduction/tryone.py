class User:
    def __init__(self, name, email, address, account_type, account_number):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = account_number
        self.balance = 0
        self.loan_taken = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")
        print(
            f"Deposited {amount} successfully. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
            print(
                f"Withdrew {amount} successfully. Current balance: {self.balance}")

    def check_balance(self):
        print(f"Available balance: {self.balance}")

    def check_transaction_history(self):
        for transaction in self.transaction_history:
            print(transaction)

    def transfer(self, recipient, amount):
        if recipient:
            if amount <= self.balance:
                self.balance -= amount
                recipient.deposit(amount)
                self.transaction_history.append(
                    f"Transferred {amount} to account {recipient.account_number}")
                print(
                    f"Transferred {amount} to account {recipient.account_number} successfully.")
            else:
                print("Insufficient balance for the transfer.")
        else:
            print("Account does not exist.")


class Admin:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

#     def create_user_account(self, name, email, address, account_type, bank):
#         bank.create_user_account(name, email, address, account_type)
#         print("User account created successfully.")

#     def delete_user_account(self, account_number, bank):
#         for user in bank.users:
#             if user.account_number == account_number:
#                 bank.users.remove(user)
#                 print(f"User account {account_number} deleted successfully.")
#                 return
#         print("User account not found.")

#     def list_user_accounts(self, bank):
#         for user in bank.users:
#             print(
#                 f"Account Number: {user.account_number}, Name: {user.name}, Balance: {user.balance}")

#     def check_total_balance(self, bank):
#         total_balance = sum(user.balance for user in bank.users)
#         return total_balance


# class Bank:
#     def __init__(self):
#         self.users = []
#         self.admin = None

#     def create_user_account(self, name, email, address, account_type):
#         account_number = len(self.users) + 1
#         user = User(name, email, address, account_type, account_number)
#         self.users.append(user)
#         print(
#             f"Account created successfully. Your account number is {account_number}")

#     def create_admin_account(self, admin_name, admin_email, admin_password):
#         self.admin = Admin(admin_name, admin_email, admin_password)
#         print("Admin account created successfully.")


# # Example usage:
# # bank = Bank()
# # admin = Admin(bank)

# bank = Bank()
# admin = Admin(bank)
# # bank.create_admin_account("Admin Name", "admin@example.com", "admin_password")
# # bank.create_admin_account()


# # while True:
# #     print("\n1. User Login")
# #     print("2. Admin Login")
# #     print("3. Exit")
# #     choice = input("Enter your choice: ")

# #     if choice == "1":
# #         account_number = int(input("Enter your account number: "))
# #         user = next(
# #             (u for u in bank.users if u.account_number == account_number), None)
# #         if user:
# #             while True:
# #                 print("\n1. Deposit")
# #                 print("2. Withdraw")
# #                 print("3. Check Balance")
# #                 print("4. Transaction History")
# #                 print("5. Transfer Money")
# #                 print("6. Logout")
# #                 user_choice = input("Enter your choice: ")

# #                 if user_choice == "1":
# #                     amount = int(input("Enter the amount to deposit: "))
# #                     user.deposit(amount)
# #                 elif user_choice == "2":
# #                     amount = int(input("Enter the amount to withdraw: "))
# #                     user.withdraw(amount)
# #                 elif user_choice == "3":
# #                     user.check_balance()
# #                 elif user_choice == "4":
# #                     user.check_transaction_history()
# #                 elif user_choice == "5":
# #                     recipient_account_number = int(
# #                         input("Enter the recipient's account number: "))
# #                     recipient = next(
# #                         (u for u in bank.users if u.account_number == recipient_account_number), None)
# #                     amount = int(input("Enter the amount to transfer: "))
# #                     user.transfer(recipient, amount)
# #                 elif user_choice == "6":
# #                     break
# #         else:
# #             print("User account not found.")
# #     elif choice == "2":
# #         admin_password = input("Enter admin password: ")
# #         admin = bank.admin
# #         if admin and admin.password == admin_password:
# #             while True:
# #                 print("\n1. Create User Account")
# #                 print("2. Delete User Account")
# #                 print("3. List User Accounts")
# #                 print("4. Check Total Balance")
# #                 print("5. Check Total Loan Amount")
# #                 print("6. Logout")
# #                 admin_choice = input("Enter your choice: ")

# #                 if admin_choice == "1":
# #                     name = input("Enter user's name: ")
# #                     email = input("Enter user's email: ")
# #                     address = input("Enter user's address: ")
# #                     account_type = input(
# #                         "Enter user's account type (Savings/Current): ").lower()
# #                     admin.create_user_account(
# #                         name, email, address, account_type, bank)
# #                 elif admin_choice == "2":
# #                     account_number = int(
# #                         input("Enter the account number to delete: "))
# #                     admin.delete_user_account(account_number, bank)
# #                 elif admin_choice == "3":
# #                     admin.list_user_accounts(bank)
# #                 elif admin_choice == "4":
# #                     total_balance = admin.check_total_balance(bank)
# #                     print(f"Total Available Balance: {total_balance}")
# #                 elif admin_choice == "5":
# #                     total_loan_amount = admin.check_total_loan_amount(bank)
# #                     print(f"Total Loan Amount: {total_loan_amount}")

# #                 elif admin_choice == "6":
# #                     break
# #         else:
# #             print("Invalid admin password.")
# #     elif choice == "3":
# #         break


# while True:
#     print("Select an option:")
#     print("1. User Options")
#     print("2. Admin Options")
#     print("3. Exit")
#     choice = input("Enter your choice: ")

#     if choice == "1":
#         print("\nUser Options:")
#         print("1. Create Account")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Check Balance")
#         print("5. Transaction History")
#         print("6. Take Loan")
#         print("7. Transfer Money")
#         print("8. Exit")
#         user_choice = input("Enter your choice: ")

#         if user_choice == "1":
#             name = input("Enter your name: ")
#             email = input("Enter your email: ")
#             address = input("Enter your address: ")
#             account_type = input("Enter account type (Savings or Current): ")
#             print(bank.create_account(name, email, address, account_type))
#         elif user_choice == "2":
#             user_id = int(input("Enter your account number: "))
#             amount = float(input("Enter the amount to deposit: "))
#             print(bank.deposit(user_id, amount))
#         elif user_choice == "3":
#             user_id = int(input("Enter your account number: "))
#             amount = float(input("Enter the amount to withdraw: "))
#             print(bank.withdraw(user_id, amount))
#         elif user_choice == "4":
#             user_id = int(input("Enter your account number: "))
#             print(bank.check_balance(user_id))
#         elif user_choice == "5":
#             user_id = int(input("Enter your account number: "))
#             print(bank.transaction_history(user_id))
#         elif user_choice == "6":
#             user_id = int(input("Enter your account number: "))
#             amount = float(input("Enter the loan amount: "))
#             print(bank.take_loan(user_id, amount))
#         elif user_choice == "7":
#             sender_id = int(input("Enter your account number: "))
#             receiver_id = int(input("Enter the receiver's account number: "))
#             amount = float(input("Enter the amount to transfer: "))
#             print(bank.transfer(sender_id, receiver_id, amount))
#         elif user_choice == "8":
#             break
#     elif choice == "2":
#         print("\nAdmin Options:")
#         print("1. Create Account")
#         print("2. Delete Account")
#         print("3. View All Accounts")
#         print("4. Check Total Balance")
#         print("5. Check Total Loan Amount")
#         print("6. Toggle Loan Feature")
#         print("7. Exit")
#         admin_choice = input("Enter your choice: ")

#         if admin_choice == "1":
#             name = input("Enter user's name: ")
#             email = input("Enter user's email: ")
#             address = input("Enter user's address: ")
#             account_type = input("Enter account type (Savings or Current): ")
#             print(admin.create_account(name, email, address, account_type))
#         elif admin_choice == "2":
#             user_id = int(input("Enter the account number to delete: "))
#             print(admin.delete_account(user_id))
#         elif admin_choice == "3":
#             print(admin.view_all_accounts())
#         elif admin_choice == "4":
#             print(admin.check_total_balance())
#         elif admin_choice == "5":
#             print(admin.check_total_loan_amount())
#         elif admin_choice == "6":
#             print(admin.toggle_loan_feature())
#         elif admin_choice == "7":
#             break
#     elif choice == "3":
#         break
#     else:
#         print("Invalid choice. Please select again.")
