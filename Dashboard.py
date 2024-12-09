class Dashboard:
    """Displays financial metrics and visualizations."""

    @staticmethod
    def display_dashboard(manager):
        print("\n===== Financial Dashboard =====")
        manager.display_summary()

    @staticmethod
    def display_graph(finances):
        labels = ['Current Balance', 'Total Spent']
        values = [finances.current_balance, finances.total_spent]

        plt.bar(labels, values, color=['green', 'red'])
        plt.title("Financial Overview")
        plt.ylabel("Amount (Taka)")
        plt.show()

    @staticmethod
    def display_expense_pie_chart(expenses):
        categories = [expense['category'] for expense in expenses]
        amounts = [expense['amount'] for expense in expenses]

        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
        plt.title("Expense Distribution")
        plt.show()
