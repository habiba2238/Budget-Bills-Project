class ExpenseManager(FinancialManager):
    """Manages expenses for the user."""

    def __init__(self, budget):
        super().__init__(budget)
        self.expenses = []

    def add_record(self, amount, category, description):
        self.expenses.append({
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'amount': amount,
            'category': category,
            'description': description
        })
        self.total_spent += amount
        self.current_balance -= amount

    def display_summary(self):
        print("\n===== Expense Summary =====")
        print(f"Total Spent: {self.total_spent} Taka")
        print(f"Remaining Balance: {self.current_balance} Taka")

    def save_expenses(self, file_path="assets/expenses.csv"):
        pd.DataFrame(self.expenses).to_csv(file_path, index=False)


class LoanManager(FinancialManager):
    """Manages loans for the user."""

    def __init__(self, budget):
        super().__init__(budget)
        self.loans = []

    def add_record(self, lender_name, amount, return_date):
        self.loans.append({
            'lender': lender_name,
            'amount': amount,
            'date_taken': datetime.now().strftime("%Y-%m-%d"),
            'return_date': return_date
        })
        self.total_deposits += amount
        self.current_balance += amount

    def display_summary(self):
        print("\n===== Loan Summary =====")
        print(f"Total Deposits: {self.total_deposits} Taka")
        print(f"Current Balance: {self.current_balance} Taka")

    def get_upcoming_loans(self):
        today = datetime.now().strftime("%Y-%m-%d")
        for loan in self.loans:
            if loan['return_date'] >= today:
                print(f"Lender: {loan['lender']}, Amount: {loan['amount']}, Return By: {loan['return_date']}")
