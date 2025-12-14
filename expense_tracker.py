import sys
import json
from datetime import date

DATA_FILE = "expenses.json"


def load_expenses():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)


def add_expense(description, amount):
    expenses = load_expenses()
    expense = {
        "id": len(expenses) + 1,
        "description": description,
        "amount": float(amount),
        "date": str(date.today())
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully.")


def list_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return

    print("ID | Date       | Description | Amount")
    print("--------------------------------------")
    for e in expenses:
        print(f"{e['id']}  | {e['date']} | {e['description']} | {e['amount']}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python expense_tracker.py <command>")
        print("Commands:")
        print("  add --description <text> --amount <number>")
        print("  list")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if "--description" not in sys.argv or "--amount" not in sys.argv:
            print("Usage: add --description <text> --amount <number>")
            sys.exit(1)

        desc_index = sys.argv.index("--description") + 1
        amt_index = sys.argv.index("--amount") + 1

        description = sys.argv[desc_index]
        amount = sys.argv[amt_index]

        add_expense(description, amount)

    elif command == "list":
        list_expenses()

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
