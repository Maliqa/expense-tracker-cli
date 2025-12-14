import sys
import json
from datetime import datetime

DATA_FILE = "expenses.json"


def load_expenses():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)


def add_expense(description, amount):
    expenses = load_expenses()

    expense = {
        "id": len(expenses) + 1,
        "description": description,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully.")


def main():
    if len(sys.argv) < 2:
        print("Usage: python expense_tracker.py <command>")
        print("Commands: add")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if "--description" not in sys.argv or "--amount" not in sys.argv:
            print("Usage: add --description <text> --amount <number>")
            sys.exit(1)

        desc_index = sys.argv.index("--description") + 1
        amt_index = sys.argv.index("--amount") + 1

        description = sys.argv[desc_index]
        amount = float(sys.argv[amt_index])

        add_expense(description, amount)

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
