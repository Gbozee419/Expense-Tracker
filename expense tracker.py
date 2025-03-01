import csv
import os

FILENAME = "expenses.csv"

# Load existing expenses from file
def load_expenses():
    if not os.path.exists(FILENAME):
        return []

    with open(FILENAME, mode='r', newline='') as file:
        reader = csv.reader(file)
        return list(reader)

# Save expenses to file
def save_expenses(expenses):
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(expenses)

# Add new expense
def add_expense(expenses):
    description = input("Enter expense description: ")
    amount = input("Enter amount: ")
    date = input("Enter date (YYYY-MM-DD): ")

    expenses.append([description, amount, date])
    print("✅ Expense added successfully!")

# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("\nAll Expenses:")
        print("{:<5} {:<20} {:<10} {:<12}".format("ID", "Description", "Amount", "Date"))
        for idx, expense in enumerate(expenses):
            print(f"{idx+1:<5} {expense[0]:<20} {expense[1]:<10} {expense[2]:<12}")
        print()

# Delete an expense
def delete_expense(expenses):
    view_expenses(expenses)
    try:
        expense_id = int(input("Enter the ID of the expense to delete: ")) - 1
        if 0 <= expense_id < len(expenses):
            removed = expenses.pop(expense_id)
            print(f"❌ Expense '{removed[0]}' deleted successfully!")
        else:
            print("Invalid expense ID.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            delete_expense(expenses)
        elif choice == '4':
            save_expenses(expenses)
            print("💾 Expenses saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
