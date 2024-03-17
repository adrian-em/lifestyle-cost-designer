import sqlite3


def initialize_database():
    connection = sqlite3.connect("file:./db.db?mode=rwc", uri=True)
    cursor = connection.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        frequency TEXT NOT NULL,
        priority INTEGER NOT NULL
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS user_settings (
        id INTEGER PRIMARY KEY CHECK (id = 1),  -- Ensures only one row for settings
        tax_rate REAL NOT NULL,
        savings_rate REAL NOT NULL,
        current_income REAL NOT NULL,
        current_expenses REAL NOT NULL
    );
    """
    )

    # Insert initial data if necessary
    cursor.execute(
        """
    INSERT OR IGNORE INTO user_settings (id, tax_rate, savings_rate, current_income, current_expenses) VALUES (1, 0, 0, 0, 0);
    """
    )

    connection.commit()
    connection.close()


if __name__ == "__main__":
    initialize_database()
    print("Database initialized.")
