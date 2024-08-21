import sqlite3
import re
import random

# Create a connection to the database
conn = sqlite3.connect("/Users/abdullahyilmaz/Desktop/Cloud-DevOps/projeler/banka uygulaması/bank_database.db")
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        surname TEXT,
        account_number TEXT,
        balance TEXT
    );
""")

def create_account():
    # Get user input
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")

    # Generate a standard account number
    account_number = f"{name[0].upper()}{surname[0].upper()}{str(random.randint(100000, 999999))}"
    print(f"Your account number is: {account_number}")

    # Get user input for balance
    while True:
        balance_input = input("Enter your initial balance: ")
        balance_input = balance_input.replace(",", ".")  # Replace commas with dots
        try:
            balance = float(balance_input)
            break
        except ValueError:
            print("Invalid balance. Please try again.")

    # Format balance as "XXX.XXX,XX €"
    balance_formatted = "{:,.2f} €".format(balance).replace('.', '#').replace(',', '.').replace('#', ',')

    # Validate account number input
    # while True:
    #     user_account_number = input("Enter your account number (must match the generated one): ")
    #     if re.match(rf"^{name[0].upper()}{surname[0].upper()}[0-9]{{6}}$", user_account_number):
    #         break
    #     print("Invalid account number. Please try again.")

    # Insert data into the table
    cursor.execute("""
        INSERT INTO customers (name, surname, account_number, balance)
        VALUES (?, ?, ?, ?);
    """, (name, surname, account_number, balance_formatted))

    # Commit the changes
    conn.commit()

    print("Account created successfully!")

def deposit_money():
    account_number = input("Enter your account number: ")
    cursor.execute("SELECT balance FROM customers WHERE account_number = ?", (account_number,))
    balance = cursor.fetchone()
    if balance:
        balance = float(balance[0].replace('.', '').replace(',', '.').replace(' €', ''))
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        balance_formatted = "{:,.2f} €".format(balance).replace('.', '#').replace(',', '.').replace('#', ',')
        
        cursor.execute("UPDATE customers SET balance = ? WHERE account_number = ?", (balance_formatted, account_number))
        conn.commit()
        print(f"Deposit successful! You added {amount:.2f} €. Your new balance is: {balance:.2f} €")
    else:
        print("Account not found!")

def withdraw_money():
    account_number = input("Enter your account number: ")
    cursor.execute("SELECT balance FROM customers WHERE account_number = ?", (account_number,))
    balance = cursor.fetchone()
    if balance:
        balance = float(balance[0].replace('.', '').replace(',', '.').replace(' €', ''))
        amount = float(input("Enter the amount to withdraw: "))
        if balance >= amount:
            balance -= amount
            balance_formatted = "{:,.2f} €".format(balance).replace('.', '#').replace(',', '.').replace('#', ',')
            print(f"Withdrawal successful! You withdrew {amount:.2f} €. Your new balance is: {balance:.2f} €")
            cursor.execute("UPDATE customers SET balance = ? WHERE account_number = ?", (balance_formatted, account_number))
            conn.commit()
        else:    
            print("Insufficient balance!")
    else:
        print("Account not found!")

def check_balance():
    account_number = input("Enter your account number: ")
    cursor.execute("SELECT balance FROM customers WHERE account_number = ?", (account_number,))
    balance = cursor.fetchone()
    if balance:
        print(f"Your balance is: {balance[0]}")
    else:
        print("Account not found!")

def delete_customer():
    account_number = input("Enter the account number to delete: ")
    cursor.execute("SELECT * FROM customers WHERE account_number = ?", (account_number,))
    customer = cursor.fetchone()
    if customer:
        confirm = input(f"Are you sure you want to delete the account {account_number} belonging to {customer[1]} {customer[2]}? (yes/no): ")
        if confirm.lower() == "yes":
            cursor.execute("DELETE FROM customers WHERE account_number = ?", (account_number,))
            conn.commit()
            print("Account deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print("Account not found!")

def main_menu():
    while True:
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Delete Customer")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            delete_customer()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

# Close the connection
conn.close()