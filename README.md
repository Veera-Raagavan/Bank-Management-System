# Bank Management System

A console-based banking application written in **Python** with a **MySQL** backend. It lets you create customer accounts, view details, deposit and withdraw money, delete accounts and list all accounts through a simple menu.

> Built as a CBSE Class 12 Computer Science project to demonstrate Python-MySQL connectivity, CRUD operations and parameterized SQL queries.

---

## Table of Contents

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Project Structure](#project-structure)
4. [Database Design](#database-design)
5. [Prerequisites](#prerequisites)
6. [Installation and Setup](#installation-and-setup)
7. [Usage](#usage)
8. [Demo Version (No Database)](#demo-version-no-database)
9. [Sample Output](#sample-output)
10. [How It Works](#how-it-works)
11. [Known Limitations](#known-limitations)
12. [Future Improvements](#future-improvements)

---

## Features

| # | Menu option | What it does |
|---|-------------|--------------|
| 1 | Create New Account | Adds an account with number, name, date of birth, address, phone and opening balance |
| 2 | Display Account Details | Shows all details of one account |
| 3 | Deposit Money | Adds an amount to an account's balance |
| 4 | Withdraw Money | Deducts an amount, blocked if the balance is insufficient |
| 5 | Delete Account | Deletes an account after a yes/no confirmation |
| 6 | Display All Accounts | Prints a table of every account with the total count |
| 7 | Exit | Closes the program |

Other highlights:

- **Automatic setup**: the `bank` database and `accounts` table are created on first run.
- **Parameterized queries** (`%s` placeholders) protect against SQL injection.
- **Duplicate check**: an account number that already exists is rejected.
- **Amount validation**: deposits and withdrawals must be greater than zero.
- **Error handling**: invalid input and database errors are caught and reported, and connections are closed in `finally` blocks.

---

## Tech Stack

- **Language:** Python 3.x
- **Database:** MySQL
- **Library:** `mysql-connector-python`

---

## Project Structure

```
bank-management-system/
├── bank_project.py        # Main application (uses MySQL)
├── bank.sql               # Optional manual database setup script
├── run_sql.bat            # Windows batch file to run bank.sql
├── execute_sql.ps1        # PowerShell helper for running the SQL script
├── bank_project_demo.py   # Demo version with in-memory data (no MySQL needed)
├── demo_output.py         # Automated demo that prints sample output
├── .gitignore
└── README.md
```

---

## Database Design

**Database name:** `bank`

### `accounts` table

| Column | Type | Constraint |
|--------|------|------------|
| acc_no | INT | PRIMARY KEY |
| name | VARCHAR(100) | NOT NULL |
| dob | DATE | NOT NULL |
| address | VARCHAR(200) | NOT NULL |
| phone | VARCHAR(15) | NOT NULL |
| balance | DECIMAL(10,2) | NOT NULL, DEFAULT 0.00 |

This is the table that `bank_project.py` creates. `bank.sql` defines the same table with slightly different sizes and a `FLOAT` balance, so see the note in the setup section.

---

## Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [MySQL Server](https://dev.mysql.com/downloads/mysql/) running on `localhost`
- The `mysql-connector-python` package

---

## Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/<your-username>/bank-management-system.git
cd bank-management-system
```

**2. Install the MySQL connector**

```bash
pip install mysql-connector-python
```

**3. Set your MySQL credentials**

Open `bank_project.py` and edit the configuration at the top:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_mysql_password',
    'database': 'bank'
}
```

**4. (Optional) Create the database manually**

The program creates the database and table by itself, so this step is not required. If you still want to run the SQL script:

```bash
mysql -u root -p < bank.sql
```

On Windows you can double-click `run_sql.bat` instead, which runs the same command and asks for your MySQL password. It needs `mysql` to be available in your system PATH.

> **Note:** run only one of the two setup routes on a fresh database. Because both use `CREATE TABLE IF NOT EXISTS`, whichever runs first decides the table definition. For the intended schema (`DECIMAL` balance), let `bank_project.py` create the table.

**5. Run the program**

```bash
python bank_project.py
```

---

## Usage

On start, the program prepares the database and shows this menu:

```
==================================================
      BANK MANAGEMENT SYSTEM
==================================================
1. Create New Account
2. Display Account Details
3. Deposit Money
4. Withdraw Money
5. Delete Account
6. Display All Accounts
7. Exit
==================================================
Enter your choice (1-7):
```

A typical workflow:

1. Choose **1** and enter the account details, for example account number `1001`, date of birth as `YYYY-MM-DD`, and an opening balance.
2. Choose **3** or **4** to deposit or withdraw money.
3. Choose **2** to check the balance, or **6** to list all accounts.
4. Choose **5** to delete an account (you must type `yes` to confirm).

---

## Demo Version (No Database)

If MySQL is not installed, or you only need screenshots for a report, use the demo files. They imitate the database with a Python dictionary, so nothing is saved after the program closes.

| File | Description |
|------|-------------|
| `bank_project_demo.py` | Fully interactive version with the same menu, starting with two sample accounts |
| `demo_output.py` | Non-interactive script that creates five accounts and prints the "All Accounts" table |

```bash
python bank_project_demo.py
python demo_output.py
```

The real application is `bank_project.py`. The demo files exist only for demonstration.

---

## Sample Output

Creating an account:

```
=== CREATE NEW ACCOUNT ===
Enter Account Number: 1001
Enter Account Holder Name: Rajesh Kumar
Enter Date of Birth (YYYY-MM-DD): 1990-05-15
Enter Address: 123 MG Road, Mumbai
Enter Phone Number: 9876543210
Enter Initial Balance: 50000

Account created successfully!
Account Number: 1001
Name: Rajesh Kumar
Balance: ₹50000.0
```

Withdrawing money:

```
=== WITHDRAW MONEY ===
Enter Account Number: 1001
Enter Amount to Withdraw: ₹5000

Withdrawal successful!
Amount Withdrawn: ₹5000
Previous Balance: ₹50000.00
New Balance: ₹45000.00
```

---

## How It Works

| Function | Purpose |
|----------|---------|
| `create_database()` | Connects without a database name and creates `bank` if missing |
| `create_table()` | Creates the `accounts` table if missing |
| `connect_database()` | Opens a connection using `DB_CONFIG`, returns `None` on failure |
| `create_account()` | Checks for a duplicate account number, then inserts a new row |
| `display_account()` | Fetches and prints one account |
| `deposit_money()` | Validates the amount, then increases the balance |
| `withdraw_money()` | Validates the amount and balance, then decreases the balance |
| `delete_account()` | Shows the account and deletes it after confirmation |
| `display_all_accounts()` | Prints every account in a formatted table |
| `main_menu()` | Runs the menu loop |

---

## Known Limitations

- The MySQL password is stored in plain text in the source code.
- Deposit and withdraw amounts must be whole numbers, so values like `500.50` are rejected.
- Balance changes are read, calculated in Python and written back, which is not safe if two sessions update the same account at once.
- The opening balance is not checked, so a negative value is accepted.
- Date of birth, phone number, name and address are not validated beyond what MySQL itself enforces.
- An account can be deleted even if it still holds money.
- There is no login, PIN or transaction history.
- The rupee symbol (`₹`) may fail to print in older Windows consoles. Running `chcp 65001` or setting `PYTHONUTF8=1` fixes this.

---

## Future Improvements

- Read credentials from environment variables or a `.env` file.
- Use `Decimal` for amounts and update balances with a single SQL statement.
- Add a `transactions` table with a mini statement for each account.
- Add fund transfer between accounts using a commit/rollback transaction.
- Add an option to update address and phone number.
- Search accounts by name, and filter by balance.
- Add a PIN for withdrawals and block deletion of accounts with a balance.
- Validate all inputs (phone digits, date range, positive account numbers).

---

## Author

**Veera Raagavan**
CBSE Class 12 Computer Science Project

---

## License

This project is intended for educational purposes. Feel free to use and modify it for learning.
