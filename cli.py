import typer
import services
from calculations import calculate_total_expenses, calculate_required_income


app = typer.Typer()


@app.command()
def add_expense(
    description: str, category: str, amount: float, frequency: str, priority: int
):
    expense = services.add_expense(description, category, amount, frequency, priority)
    typer.echo(f"Added expense: {expense.model_dump()}")


@app.command()
def list_expenses():
    expenses = services.list_expenses()
    for expense in expenses:
        # typer.echo(f"{expense.description} - {expense.category} - {expense.amount} ({expense.frequency})")
        typer.echo(expense.model_dump())


@app.command()
def update_settings(
    tax_rate: float, savings_rate: float, current_income: float, current_expenses: float
):
    settings = services.update_settings(
        tax_rate, savings_rate, current_income, current_expenses
    )
    typer.echo(f"Updated settings: {settings.model_dump()}")


@app.command()
def get_settings():
    settings = services.get_settings()
    if settings:
        typer.echo(
            f"Tax Rate: {settings.tax_rate}%, Savings Rate: {settings.savings_rate}%, Current Income: {settings.current_income}, Current Expenses: {settings.current_expenses}"
        )
    else:
        typer.echo("Settings not found")


@app.command()
def calculate_required_monthly_income():
    expenses = services.list_expenses()
    settings = services.get_settings()
    if (
        not settings
        or settings.current_income is None
        or settings.current_expenses is None
    ):
        typer.echo(
            "User settings incomplete. Please set current income, current expenses, tax rate, and savings rate."
        )
        raise typer.Exit(code=1)

    total_expenses = calculate_total_expenses(expenses) + settings.current_expenses
    total_income_needed = calculate_required_income(
        total_expenses, settings.tax_rate, settings.savings_rate
    )

    typer.echo(f"Total monthly expenses: {total_expenses:.2f}")
    typer.echo(
        f"Total monthly income needed before taxes and savings: {total_income_needed:.2f}"
    )

    current_disposable_income = settings.current_income - settings.current_expenses
    if current_disposable_income < total_expenses:
        additional_income_needed = (total_expenses - settings.current_expenses) - current_disposable_income

        percentage_increase_needed = (
            (total_income_needed - settings.current_income) / settings.current_income
        ) * 100
        typer.echo(f"Additional monthly income needed: {additional_income_needed:.2f}")
        typer.echo(
            f"Percentage increase needed in current income: {percentage_increase_needed:.2f}%"
        )
    else:
        typer.echo(
            "Your current disposable income is sufficient to afford your desired lifestyle."
        )


@app.command()
def cli_delete_expense(expense_id: int):
    try:
        services.delete_expense(expense_id)
        typer.echo(f"Expense with ID {expense_id} successfully deleted.")
    except Exception as e:
        typer.echo(f"Error: {str(e)}")


if __name__ == "__main__":
    app()
