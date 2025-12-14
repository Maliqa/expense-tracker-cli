import sys
import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"


# ---------------------------
# Utilities
# ---------------------------
def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)


def generate_id(expenses):
    if not expenses:
        return 1
    return max(exp["id"] for exp in expenses) + 1


# ---------------------------
# Commands
# ---------------------------
def add_expense(args):
    if "--description" not in args or "--amount" not in args:
        print("Usage: python expense_tracker.py add --description <text> --amount <number>")
        return

    description = args[args.index("--description") + 1]
    amount = float(args[args.index("--amount") + 1])

    expenses = load_expenses()

    expense = {
        "id": generate_id(expenses),
        "description": description,
        "amount": amount,
        "date": datetime.today().strftime("%Y-%m-%d")
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
    for exp in expenses:
        print(f"{exp['id']} | {exp['date']} | {exp['description']} | {exp['amount']}")


def summary(args):
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    # summary --month <MM>
    if "--month" in args:
        month = args[args.index("--month") + 1]
        total = sum(
            exp["amount"]
            for exp in expenses
            if exp["date"].split("-")[1] == month
        )
        print(f"Total expenses for month {month}: {total}")
    else:
        total = sum(exp["amount"] for exp in expenses)
        print(f"Total expenses: {total}")


# ---------------------------
# Main CLI
# ---------------------------
def main():
    if len(sys.argv) < 2:
        print("Usage: python expense_tracker.py <command>")
        print("Commands:")
        print("  add")
        print("  list")
        print("  summary")
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "add":
        add_expense(args)
    elif command == "list":
        list_expenses()
    elif command == "summary":
        summary(args)
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
