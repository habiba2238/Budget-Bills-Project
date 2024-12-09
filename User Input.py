class DataInput:
    """Handles user input for financial data."""

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
        try:
            expense = float(input("Enter your expense amount: "))
            category = input("Enter the category of the expense (e.g., food, rent): ")
            description = input("Enter a description for the expense: ")
            return expense, category, description
        except ValueError:
            print("Invalid input. Please try again.")

    @staticmethod
    def get_loan_input():
        lender_name = input("Enter lender name: ")
        try:
            amount = float(input("Enter loan amount: "))
            return_date = input("Enter loan return date (YYYY-MM-DD): ")
            return lender_name, amount, return_date
        except ValueError:
            print("Invalid input. Please try again.")
