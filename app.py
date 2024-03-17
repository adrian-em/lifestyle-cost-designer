from flask import Flask, request, jsonify
from models import Expense, UserSettings
import services
from pydantic import ValidationError
from calculations import calculate_total_expenses, calculate_required_income


app = Flask(__name__)


@app.post("/expenses/")
def add_expense():
    try:
        expense_data = Expense(**request.json)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    expense = services.add_expense(
        expense_data.description,
        expense_data.category,
        expense_data.amount,
        expense_data.frequency,
        expense_data.priority,
    )
    return jsonify(expense.model_dump()), 201


@app.get("/expenses/")
def list_expenses():
    expenses = services.list_expenses()
    return jsonify([expense.model_dump() for expense in expenses])


@app.post("/settings/")
def update_settings():
    try:
        settings_data = UserSettings(**request.json)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    settings = update_settings(
        settings_data.tax_rate,
        settings_data.savings_rate,
        settings_data.current_income,
        settings_data.current_expenses,
    )

    return jsonify(settings.model_dump()), 201


@app.get("/settings/")
def get_settings():
    settings = services.get_settings()
    return jsonify(settings.model_dump()) if settings else ("", 404)


@app.get("/required_income/")
def get_required_income():
    expenses = services.list_expenses()
    settings = services.get_settings()
    if (
        not settings
        or settings.current_income is None
        or settings.current_expenses is None
    ):
        return {
            "error": "User settings incomplete. Please set current income, current expenses, tax rate, and savings rate."
        }, 404

    total_expenses = calculate_total_expenses(expenses)
    total_income_needed = calculate_required_income(
        total_expenses, settings.tax_rate, settings.savings_rate
    )

    # Calculate current disposable income (current income after current expenses)
    current_disposable_income = settings.current_income - settings.current_expenses
    additional_income_needed = max(
        0, total_expenses - current_disposable_income
    )  # Ensure this doesn't go negative
    percentage_increase_needed = 0
    if settings.current_income < total_income_needed:
        percentage_increase_needed = (
            (total_income_needed - settings.current_income) / settings.current_income
        ) * 100

    return {
        "total_monthly_expenses": total_expenses,
        "required_monthly_income_before_taxes_savings": total_income_needed,
        "additional_monthly_income_needed": additional_income_needed,
        "percentage_increase_needed_in_current_income": percentage_increase_needed,
    }


@app.delete("/expenses/{expense_id}")
def api_delete_expense(expense_id: int):
    try:
        services.delete_expense(expense_id)
        return {"message": "Expense successfully deleted"}, 200
    except Exception as e:
        return {"error": str(e)}, 404


if __name__ == "__main__":
    app.run(debug=True)
