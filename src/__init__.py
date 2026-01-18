import json
from pathlib import Path

DATA_FILE = Path("data/expenses.json")

def load_expenses():
    if not DATA_FILE.exists():
        return []
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))

def save_expenses(expenses):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(expenses, indent=2), encoding="utf-8")

def add_expense(expenses, title, amount):
    expenses.append({"title": title, "amount": amount})
    save_expenses(expenses)

def total(expenses):
    return sum(e["amount"] for e in expenses)

def main():
    expenses = load_expenses()

    while True:
        print("\n=== CLI Expense Tracker ===")
        print("1) Add expense")
        print("2) Show all expenses")
        print("3) Show total")
        print("4) Exit")

        choice = input("Select option (1-4): ").strip()

        if choice == "1":
            title = input("Expense title: ").strip()
            amount_str = input("Amount (e.g., 12.5): ").strip()
            try:
                amount = float(amount_str)
            except ValueError:
                print("❌ Invalid amount. Please enter a number.")
                continue

            add_expense(expenses, title, amount)
            print("✅ Expense added!")

        elif choice == "2":
            if not expenses:
                print("No expenses yet.")
            else:
                print("\n--- Expenses ---")
                for i, e in enumerate(expenses, start=1):
                    print(f"{i}. {e['title']} - {e['amount']}")
        elif choice == "3":
            print(f"Total = {total(expenses)}")
        elif choice == "4":
            print("Bye 👋")
            break
        else:
            print("❌ Please choose 1-4 only.")

if __name__ == "__main__":
    main()
