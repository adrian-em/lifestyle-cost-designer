from typing import List
from models import Expense

def calculate_monthly_expense(expense: Expense) -> float:
    """Converts an individual expense to its monthly equivalent."""
    if expense.frequency == 'weekly':
        return expense.amount * 4
    elif expense.frequency == 'daily':
        return expense.amount * 30
    elif expense.frequency == 'yearly':
        return expense.amount / 12
    return expense.amount

def calculate_total_expenses(expenses: List[Expense]) -> float:
    """Converts all expenses to a monthly equivalent, sums them up."""
    return sum(calculate_monthly_expense(expense) for expense in expenses)

def calculate_required_income(total_expenses: float, tax_rate: float, savings_rate: float) -> float:
    """Calculate the gross total income needed considering tax and savings rates."""
    if tax_rate < 0 or tax_rate >= 100 or savings_rate < 0:
        raise ValueError("Invalid tax rate or savings rate provided.")
    
    # Convert rates from percentages to decimals
    tax_rate_decimal = tax_rate / 100
    savings_rate_decimal = savings_rate / 100

    net_income_needed = total_expenses / (1 - savings_rate_decimal)

    # Calculate the gross income needed before tax
    gross_income_needed = net_income_needed / (1 - tax_rate_decimal)
    
    return gross_income_needed
