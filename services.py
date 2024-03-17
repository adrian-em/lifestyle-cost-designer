from database import get_db
from models import Expense, UserSettings


def add_expense(
    description: str, category: str, amount: float, frequency: str, priority: int
) -> Expense:
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO expenses (description, category, amount, frequency, priority) VALUES (?, ?, ?, ?, ?)",
        (description, category, amount, frequency, priority),
    )
    db.commit()
    return Expense(
        id=cursor.lastrowid,
        description=description,
        category=category,
        amount=amount,
        frequency=frequency,
        priority=priority,
    )


def list_expenses() -> list:
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    return [
        Expense(
            id=e["id"],
            description=e["description"],
            category=e["category"],
            amount=e["amount"],
            frequency=e["frequency"],
            priority=e["priority"],
        )
        for e in expenses
    ]


def update_settings(
    tax_rate: float, savings_rate: float, current_income: float, current_expenses: float
) -> UserSettings:
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        """
        REPLACE INTO user_settings (id, tax_rate, savings_rate, current_income, current_expenses) 
        VALUES (1, ?, ?, ?, ?)
        """,
        (tax_rate, savings_rate, current_income, current_expenses),
    )
    db.commit()
    return UserSettings(
        tax_rate=tax_rate,
        savings_rate=savings_rate,
        current_income=current_income,
        current_expenses=current_expenses,
    )


def get_settings() -> UserSettings:
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user_settings WHERE id = 1")
    settings = cursor.fetchone()
    if settings:
        return UserSettings(**settings)
    return None


def delete_expense(expense_id: int) -> None:
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    db.commit()
