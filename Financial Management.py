from abc import ABC, abstractmethod
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


class FinancialManager(ABC):
    """Abstract base class for managing financial operations."""

    def __init__(self, budget):
        self.budget = budget
        self.total_spent = 0
        self.total_deposits = 0
        self.current_balance = budget

    @abstractmethod
    def add_record(self, *args, **kwargs):
        pass

    @abstractmethod
    def display_summary(self):
        pass

    def calculate_daily_limit(self, days_remaining):
        if days_remaining <= 0:
            return 0
        return self.current_balance / days_remaining
