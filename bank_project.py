import mysql.connector
from datetime import datetime

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'bank'
}

def create_database():
    """Create the 'bank' database if it doesn't exist"""
    try:
        # Connect without specifying database
        conn = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )
        cursor = conn.cursor()
        
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS bank")
        print("Database 'bank' created successfully (or already exists)")
        
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")
        return False

def create_table():
    """Create the 'accounts' table if it doesn't exist"""
    conn = connect_database()
    if conn is None:
        return False
    
    cursor = conn.cursor()
    
    try:
        # Create accounts table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS accounts (
            acc_no INT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            dob DATE NOT NULL,
            address VARCHAR(200) NOT NULL,
            phone VARCHAR(15) NOT NULL,
            balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00
        )
        """
        cursor.execute(create_table_query)
        conn.commit()
        print("Table 'accounts' created successfully (or already exists)")
        
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")
        cursor.close()
        conn.close()
        return False

def connect_database():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None

def create_account():
    conn = connect_database()
    if conn is None:
        return
    
    cursor = conn.cursor()
    
    try:
        print("\n=== CREATE NEW ACCOUNT ===")
        
        acc_no = int(input("Enter Account Number: "))
        
        cursor.execute("SELECT * FROM accounts WHERE acc_no = %s", (acc_no,))
        if cursor.fetchone():
            print(f"Account number {acc_no} already exists!")
            conn.close()
            return
        
        name = input("Enter Account Holder Name: ")
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")
        address = input("Enter Address: ")
        phone = input("Enter Phone Number: ")
        balance = float(input("Enter Initial Balance: "))
        
        query = "INSERT INTO accounts (acc_no, name, dob, address, phone, balance) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (acc_no, name, dob, address, phone, balance)
        cursor.execute(query, values)
        conn.commit()
        
        print(f"\nAccount created successfully!")
        print(f"Account Number: {acc_no}")
        print(f"Name: {name}")
        print(f"Balance: ₹{balance}")
        
    except ValueError:
        print("Invalid input! Please enter correct data types.")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        cursor.close()
        conn.close()

def display_account():
    conn = connect_database()
    if conn is None:
        return
    
    cursor = conn.cursor()
    
    try:
        print("\n=== DISPLAY ACCOUNT DETAILS ===")
        acc_no = int(input("Enter Account Number: "))
        
        query = "SELECT * FROM accounts WHERE acc_no = %s"
        cursor.execute(query, (acc_no,))
        account = cursor.fetchone()
        
        if account:
            print("\n--- Account Details ---")
            print(f"Account Number: {account[0]}")
            print(f"Name: {account[1]}")
            print(f"Date of Birth: {account[2]}")
            print(f"Address: {account[3]}")
            print(f"Phone: {account[4]}")
            print(f"Balance: ₹{account[5]}")
        else:
            print(f"Account number {acc_no} not found!")
            
    except ValueError:
        print("Invalid input! Please enter a valid account number.")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        cursor.close()
        conn.close()

def deposit_money():
    conn = connect_database()
    if conn is None:
        return
    
    cursor = conn.cursor()
    
    try:
        print("\n=== DEPOSIT MONEY ===")
        acc_no = int(input("Enter Account Number: "))
        amount = int(input("Enter Amount to Deposit: ₹"))
        
        if amount <= 0:
            print("Invalid amount! Amount must be greater than zero.")
            conn.close()
            return
        
        cursor.execute("SELECT balance FROM accounts WHERE acc_no = %s", (acc_no,))
        result = cursor.fetchone()
        
        if result:
            new_balance = result[0] + amount
            query = "UPDATE accounts SET balance = %s WHERE acc_no = %s"
            cursor.execute(query, (new_balance, acc_no))
            conn.commit()
            
            print(f"\nDeposit successful!")
            print(f"Amount Deposited: ₹{amount}")
            print(f"Previous Balance: ₹{result[0]}")
            print(f"New Balance: ₹{new_balance}")
        else:
            print(f"Account number {acc_no} not found!")
            
    except ValueError:
        print("Invalid input! Please enter correct values.")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        cursor.close()
        conn.close()

def withdraw_money():
    conn = connect_database()
    if conn is None:
        return
    
    cursor = conn.cursor()
    
    try:
        print("\n=== WITHDRAW MONEY ===")
        acc_no = int(input("Enter Account Number: "))
        amount = int(input("Enter Amount to Withdraw: ₹"))
        
        if amount <= 0:
            print("Invalid amount! Amount must be greater than zero.")
            conn.close()
            return
        
        cursor.execute("SELECT balance FROM accounts WHERE acc_no = %s", (acc_no,))
        result = cursor.fetchone()
        
        if result:
            current_balance = result[0]
            
            if current_balance >= amount:
                new_balance = current_balance - amount
                query = "UPDATE accounts SET balance = %s WHERE acc_no = %s"
                cursor.execute(query, (new_balance, acc_no))
                conn.commit()
                
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
            
    except ValueError:
        print("Invalid input! Please enter correct values.")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        cursor.close()
        conn.close()

def delete_account():
    conn = connect_database()
    if conn is None:
        return
    
    cursor = conn.cursor()
    
    try:
        print("\n=== DELETE ACCOUNT ===")
        acc_no = int(input("Enter Account Number to Delete: "))
        
        cursor.execute("SELECT * FROM accounts WHERE acc_no = %s", (acc_no,))
        account = cursor.fetchone()
        
        if account:
            print(f"\nAccount Found:")
            print(f"Name: {account[1]}")
            print(f"Balance: ₹{account[5]}")
            
            confirm = input("\nAre you sure you want to delete this account? (yes/no): ").lower()
            
            if confirm == 'yes':
                query = "DELETE FROM accounts WHERE acc_no = %s"
                cursor.execute(query, (acc_no,))
                conn.commit()
                print(f"\nAccount {acc_no} deleted successfully!")
            else:
                print("Deletion cancelled.")
        else:
            print(f"Account number {acc_no} not found!")
            
    except ValueError:
        print("Invalid input! Please enter a valid account number.")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        cursor.close()
        conn.close()

def display_all_accounts():
    conn = connect_database()
    if conn is None:
        return
    
    cursor = conn.cursor()
    
    try:
        print("\n=== ALL ACCOUNTS ===")
        
        query = "SELECT * FROM accounts"
        cursor.execute(query)
        accounts = cursor.fetchall()
        
        if accounts:
            print("\n" + "="*100)
            print(f"{'Acc No':<10} {'Name':<20} {'DOB':<12} {'Address':<25} {'Phone':<15} {'Balance':<10}")
            print("="*100)
            
            for account in accounts:
                print(f"{account[0]:<10} {account[1]:<20} {str(account[2]):<12} {account[3]:<25} {account[4]:<15} ₹{account[5]:<10}")
            
            print("="*100)
            print(f"\nTotal Accounts: {len(accounts)}")
        else:
            print("No accounts found in the database.")
            
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        cursor.close()
        conn.close()

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
    print("Initializing database...")
    
    # Create database if it doesn't exist
    if create_database():
        # Create table if it doesn't exist
        if create_table():
            print("\nDatabase setup completed successfully!")
        else:
            print("\nError setting up table. Please check MySQL connection.")
            exit(1)
    else:
        print("\nError setting up database. Please check MySQL connection.")
        exit(1)
    
    print("\n" + "="*50)
    main_menu()
