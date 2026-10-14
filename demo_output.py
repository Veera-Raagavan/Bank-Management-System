# Automated demo script to show program output
from datetime import datetime

# Simulated database storage
accounts_db = {}

def create_account(acc_no, name, dob, address, phone, balance):
    print("\n=== CREATE NEW ACCOUNT ===")
    print(f"Enter Account Number: {acc_no}")
    
    if acc_no in accounts_db:
        print(f"Account number {acc_no} already exists!")
        return
    
    print(f"Enter Account Holder Name: {name}")
    print(f"Enter Date of Birth (YYYY-MM-DD): {dob}")
    print(f"Enter Address: {address}")
    print(f"Enter Phone Number: {phone}")
    print(f"Enter Initial Balance: {balance}")
    
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

def display_account(acc_no):
    print("\n=== DISPLAY ACCOUNT DETAILS ===")
    print(f"Enter Account Number: {acc_no}")
    
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

def deposit_money(acc_no, amount):
    print("\n=== DEPOSIT MONEY ===")
    print(f"Enter Account Number: {acc_no}")
    print(f"Enter Amount to Deposit: ₹{amount}")
    
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

def withdraw_money(acc_no, amount):
    print("\n=== WITHDRAW MONEY ===")
    print(f"Enter Account Number: {acc_no}")
    print(f"Enter Amount to Withdraw: ₹{amount}")
    
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

if __name__ == "__main__":
    print("Welcome to Bank Management System!")
    print("="*50)
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
    
    print("\n")
    
    # Add 5 customers to the database
    print("Choice: 1")
    create_account(1001, "Rajesh Kumar", "1990-05-15", "123 MG Road, Mumbai", "9876543210", 50000.00)
    print("\n" + "-"*50)
    
    print("\nChoice: 1")
    create_account(1002, "Priya Sharma", "1985-08-22", "456 Park Avenue, Delhi", "9876543211", 75000.00)
    print("\n" + "-"*50)
    
    print("\nChoice: 1")
    create_account(1003, "Amit Patel", "1992-03-10", "789 Sector 5, Bangalore", "9876543212", 30000.00)
    print("\n" + "-"*50)
    
    print("\nChoice: 1")
    create_account(1004, "Sneha Reddy", "1988-11-25", "321 Tech Park, Hyderabad", "9876543213", 45000.00)
    print("\n" + "-"*50)
    
    print("\nChoice: 1")
    create_account(1005, "Vikram Singh", "1995-07-08", "654 MG Road, Pune", "9876543214", 60000.00)
    print("\n" + "-"*50)
    
    # Display all accounts
    print("\nChoice: 6")
    display_all_accounts()
    print("\n" + "-"*50)

