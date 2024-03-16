from flask import Flask, request, jsonify
from models import Expense, UserSettings
from services import add_expense, list_expenses, update_settings, get_settings
from pydantic import ValidationError

app = Flask(__name__)


@app.post("/expenses/")
def api_add_expense():
    try:
        expense_data = Expense(**request.json)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    expense = add_expense(
        expense_data.description,
        expense_data.category,
        expense_data.amount,
        expense_data.frequency,
        expense_data.priority,
    )
    return jsonify(expense.model_dump()), 201


@app.get("/expenses/")
def api_list_expenses():
    expenses = list_expenses()
    return jsonify([expense.model_dump() for expense in expenses])


@app.post("/settings/")
def api_update_settings():
    try:
        settings_data = UserSettings(**request.json)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    settings = update_settings(settings_data.tax_rate, settings_data.savings_rate)
    return jsonify(settings.model_dump()), 201


@app.get("/settings/")
def api_get_settings():
    settings = get_settings()
    return jsonify(settings.model_dump()) if settings else ("", 404)


if __name__ == "__main__":
    app.run(debug=True)
