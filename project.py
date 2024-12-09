from abc import ABC, abstractmethod
from datetime import datetime
import pandas as pd
import os
import matplotlib.pyplot as plt


class FinancialManager(ABC):
    """Abstract base class for financial operations."""

    def __init__(self, budget):
        self.__budget = budget
        self.__current_balance = budget
        self.__total_spent = 0
        self.__total_deposits = 0

    # Encapsulation: Getters and setters
    def get_budget(self):
        return self.__budget

    def get_current_balance(self):
        return self.__current_balance

    def set_current_balance(self, balance):
        self.__current_balance = balance

    def get_total_spent(self):
        return self.__total_spent

    def add_to_total_spent(self, amount):
        self.__total_spent += amount

    def get_total_deposits(self):
        return self.__total_deposits

    def add_to_total_deposits(self, amount):
        self.__total_deposits += amount

    @abstractmethod
    def add_record(self, *args, **kwargs):
        pass

    @abstractmethod
    def display_summary(self):
        pass

    def calculate_daily_limit(self, days_remaining):
        if days_remaining <= 0:
            return 0
        return self.__current_balance / days_remaining


class ExpenseManager(FinancialManager):
    """Manages expenses."""

    def __init__(self, budget):
        super().__init__(budget)
        self.__expenses = []

    # Encapsulation: Getter for expenses
    def get_expenses(self):
        return self.__expenses

    def add_record(self, amount, category, description):
        self.__expenses.append({
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'amount': amount,
            'category': category,
            'description': description
        })
        self.add_to_total_spent(amount)
        self.set_current_balance(self.get_current_balance() - amount)

    def display_summary(self):
        print("\n===== Expense Summary =====")
        print(f"Total Spent: {self.get_total_spent()} Taka")
        print(f"Remaining Balance: {self.get_current_balance()} Taka")

    def save_expenses(self, file_path="expenses.csv"):
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        df = pd.DataFrame(self.__expenses)
        df.to_csv(file_path, index=False)
        print(f"Expenses saved to {file_path}")


class LoanManager(FinancialManager):
    """Manages loans."""

    def __init__(self, budget):
        super().__init__(budget)
        self.__loans = []

    # Encapsulation: Getter for loans
    def get_loans(self):
        return self.__loans

    def add_record(self, lender_name, amount, return_date):
        try:
            datetime.strptime(return_date, "%Y-%m-%d")
            self.__loans.append({
                'lender': lender_name,
                'amount': amount,
                'date_taken': datetime.now().strftime("%Y-%m-%d"),
                'return_date': return_date
            })
            self.add_to_total_deposits(amount)
            self.set_current_balance(self.get_current_balance() + amount)
        except ValueError:
            print("Invalid date format. Please enter return date as YYYY-MM-DD.")

    def display_summary(self):
        print("\n===== Loan Summary =====")
        print(f"Total Deposits: {self.get_total_deposits()} Taka")
        print(f"Current Balance: {self.get_current_balance()} Taka")

    def get_upcoming_loans(self):
        today = datetime.now().strftime("%Y-%m-%d")
        print("\n===== Upcoming Loans =====")
        for loan in self.__loans:
            if loan['return_date'] >= today:
                print(f"Lender: {loan['lender']}, Amount: {loan['amount']}, Return By: {loan['return_date']}")


class Dashboard:
    """Displays visualizations for finances."""

    @staticmethod
    def display_dashboard(manager):
        manager.display_summary()

    @staticmethod
    def display_graph(manager):
        labels = ['Current Balance', 'Total Spent']
        values = [manager.get_current_balance(), manager.get_total_spent()]

        plt.bar(labels, values, color=['green', 'red'])
        plt.title("Financial Overview")
        plt.ylabel("Amount (Taka)")
        plt.show()

    @staticmethod
    def display_pie_chart(manager):
        expenses = manager.get_expenses()
        if not expenses:
            print("No expenses to display in the pie chart.")
            return

        categories = [exp['category'] for exp in expenses]
        amounts = [exp['amount'] for exp in expenses]

        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
        plt.title("Expense Distribution")
        plt.show()


class DataInput:
    """Handles user input."""

    @staticmethod
    def get_initial_budget():
        while True:
            try:
                budget = float(input("Enter your initial budget (Taka): "))
                if budget <= 0:
                    raise ValueError("Budget must be a positive number.")
                return budget
            except ValueError as e:
                print(e)

    @staticmethod
    def get_expense_input():
        while True:
            try:
                amount = float(input("Enter expense amount: "))
                category = input("Enter category (e.g., food, rent): ")
                description = input("Enter description: ")
                return amount, category, description
            except ValueError:
                print("Invalid input. Please try again.")

    @staticmethod
    def get_loan_input():
        while True:
            try:
                lender_name = input("Enter lender name: ")
                amount = float(input("Enter loan amount: "))
                return_date = input("Enter return date (YYYY-MM-DD): ")
                return lender_name, amount, return_date
            except ValueError:
                print("Invalid input. Please try again.")


def main():
    print("Welcome to Personal Finance Tracker!")
    data_input = DataInput()

    # Set initial budget
    budget = data_input.get_initial_budget()
    expense_manager = ExpenseManager(budget)
    loan_manager = LoanManager(budget)
    dashboard = Dashboard()

    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. Add Loan")
        print("3. View Dashboard")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            amount, category, description = data_input.get_expense_input()
            expense_manager.add_record(amount, category, description)

        elif choice == "2":
            lender_name, amount, return_date = data_input.get_loan_input()
            loan_manager.add_record(lender_name, amount, return_date)

        elif choice == "3":
            print("\n===== Dashboard =====")
            dashboard.display_dashboard(expense_manager)
            dashboard.display_dashboard(loan_manager)
            dashboard.display_graph(expense_manager)

        elif choice == "4":
            print("Exiting... Have a good day!")
            expense_manager.save_expenses()
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
