import typer
from services import add_expense, list_expenses, update_settings, get_settings

app = typer.Typer()


@app.command()
def cli_add_expense(description: str, category: str, amount: float, frequency: str, priority: int):
    expense = add_expense(description, category, amount, frequency, priority)
    typer.echo(f"Added expense: {expense.model_dump()}")


@app.command()
def cli_list_expenses():
    expenses = list_expenses()
    for expense in expenses:
        typer.echo(f"{expense.category} - {expense.amount} ({expense.frequency})")


@app.command()
def cli_update_settings(tax_rate: float, savings_rate: float):
    settings = update_settings(tax_rate, savings_rate)
    typer.echo(f"Updated settings: {settings.model_dump()}")


@app.command()
def cli_get_settings():
    settings = get_settings()
    if settings:
        typer.echo(
            f"Tax Rate: {settings.tax_rate}%, Savings Rate: {settings.savings_rate}%"
        )
    else:
        typer.echo("Settings not found")


if __name__ == "__main__":
    app()
