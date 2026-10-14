# Demo version for screenshot - simulates database operations
from datetime import datetime

# Simulated database storage
accounts_db = {
    1001: {
        'acc_no': 1001,
        'name': 'Rajesh Kumar',
        'dob': '1990-05-15',
        'address': '123 MG Road, Mumbai',
        'phone': '9876543210',
        'balance': 50000.00
    },
    1002: {
        'acc_no': 1002,
        'name': 'Priya Sharma',
        'dob': '1985-08-22',
        'address': '456 Park Avenue, Delhi',
        'phone': '9876543211',
        'balance': 75000.00
    }
}

def create_account():
    print("\n=== CREATE NEW ACCOUNT ===")
    
    acc_no = int(input("Enter Account Number: "))
    
    if acc_no in accounts_db:
        print(f"Account number {acc_no} already exists!")
        return
    
    name = input("Enter Account Holder Name: ")
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")
    address = input("Enter Address: ")
    phone = input("Enter Phone Number: ")
    balance = float(input("Enter Initial Balance: "))
    
    accounts_db[acc_no] = {
        'acc_no': acc_no,
        'name': name,
        'dob': dob,
        'address': address,
        'phone': phone,
        'balance': balance
    }
    
    print(f"\nAccount created successfully!")
    print(f"Account Number: {acc_no}")
    print(f"Name: {name}")
    print(f"Balance: ₹{balance}")

def display_account():
    print("\n=== DISPLAY ACCOUNT DETAILS ===")
    acc_no = int(input("Enter Account Number: "))
    
    if acc_no in accounts_db:
        account = accounts_db[acc_no]
        print("\n--- Account Details ---")
        print(f"Account Number: {account['acc_no']}")
        print(f"Name: {account['name']}")
        print(f"Date of Birth: {account['dob']}")
        print(f"Address: {account['address']}")
        print(f"Phone: {account['phone']}")
        print(f"Balance: ₹{account['balance']}")
    else:
        print(f"Account number {acc_no} not found!")

def deposit_money():
    print("\n=== DEPOSIT MONEY ===")
    acc_no = int(input("Enter Account Number: "))
    amount = float(input("Enter Amount to Deposit: ₹"))
    
    if amount <= 0:
        print("Invalid amount! Amount must be greater than zero.")
        return
    
    if acc_no in accounts_db:
        account = accounts_db[acc_no]
        previous_balance = account['balance']
        new_balance = previous_balance + amount
        account['balance'] = new_balance
        
        print(f"\nDeposit successful!")
        print(f"Amount Deposited: ₹{amount}")
        print(f"Previous Balance: ₹{previous_balance}")
        print(f"New Balance: ₹{new_balance}")
    else:
        print(f"Account number {acc_no} not found!")

def withdraw_money():
    print("\n=== WITHDRAW MONEY ===")
    acc_no = int(input("Enter Account Number: "))
    amount = float(input("Enter Amount to Withdraw: ₹"))
    
    if amount <= 0:
        print("Invalid amount! Amount must be greater than zero.")
        return
    
    if acc_no in accounts_db:
        account = accounts_db[acc_no]
        current_balance = account['balance']
        
        if current_balance >= amount:
            new_balance = current_balance - amount
            account['balance'] = new_balance
            
            print(f"\nWithdrawal successful!")
            print(f"Amount Withdrawn: ₹{amount}")
            print(f"Previous Balance: ₹{current_balance}")
            print(f"New Balance: ₹{new_balance}")
        else:
            print(f"Insufficient balance!")
            print(f"Current Balance: ₹{current_balance}")
            print(f"Required Amount: ₹{amount}")
    else:
        print(f"Account number {acc_no} not found!")

def delete_account():
    print("\n=== DELETE ACCOUNT ===")
    acc_no = int(input("Enter Account Number to Delete: "))
    
    if acc_no in accounts_db:
        account = accounts_db[acc_no]
        print(f"\nAccount Found:")
        print(f"Name: {account['name']}")
        print(f"Balance: ₹{account['balance']}")
        
        confirm = input("\nAre you sure you want to delete this account? (yes/no): ").lower()
        
        if confirm == 'yes':
            del accounts_db[acc_no]
            print(f"\nAccount {acc_no} deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print(f"Account number {acc_no} not found!")

def display_all_accounts():
    print("\n=== ALL ACCOUNTS ===")
    
    if accounts_db:
        print("\n" + "="*100)
        print(f"{'Acc No':<10} {'Name':<20} {'DOB':<12} {'Address':<25} {'Phone':<15} {'Balance':<10}")
        print("="*100)
        
        for acc_no in sorted(accounts_db.keys()):
            account = accounts_db[acc_no]
            print(f"{account['acc_no']:<10} {account['name']:<20} {account['dob']:<12} {account['address']:<25} {account['phone']:<15} ₹{account['balance']:<10}")
        
        print("="*100)
        print(f"\nTotal Accounts: {len(accounts_db)}")
    else:
        print("No accounts found in the database.")

def main_menu():
    while True:
        print("\n" + "="*50)
        print("      BANK MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Create New Account")
        print("2. Display Account Details")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Delete Account")
        print("6. Display All Accounts")
        print("7. Exit")
        print("="*50)
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            create_account()
        elif choice == '2':
            display_account()
        elif choice == '3':
            deposit_money()
        elif choice == '4':
            withdraw_money()
        elif choice == '5':
            delete_account()
        elif choice == '6':
            display_all_accounts()
        elif choice == '7':
            print("\nThank you for using Bank Management System!")
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 7.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    print("Welcome to Bank Management System!")
    print("Demo Version - No database required")
    main_menu()

