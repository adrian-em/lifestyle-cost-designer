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
            category=e["category"],
            amount=e["amount"],
            frequency=e["frequency"],
            priority=e["priority"],
        )
        for e in expenses
    ]


def update_settings(tax_rate: float, savings_rate: float) -> UserSettings:
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "REPLACE INTO user_settings (id, tax_rate, savings_rate) VALUES (1, ?, ?)",
        (tax_rate, savings_rate),
    )
    db.commit()
    return UserSettings(tax_rate=tax_rate, savings_rate=savings_rate)


def get_settings() -> UserSettings:
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user_settings WHERE id = 1")
    settings = cursor.fetchone()
    return (
        UserSettings(
            tax_rate=settings["tax_rate"], savings_rate=settings["savings_rate"]
        )
        if settings
        else None
    )
