# Lifestyle Cost Calculator

The Lifestyle Cost Calculator is a financial tool designed to help users understand the gross total income needed to afford their desired lifestyle, taking into account their current financial situation and goals. It factors in various expenses, tax rates, and savings rates to provide a comprehensive view of the required income.

## Financial Principle

The core financial principle behind this calculator is aimed at empowering users to bridge the gap between their current financial status and their lifestyle goals. This involves:

1. **Calculating Total Monthly Expenses**: Aggregating all individual lifestyle expenses to understand monthly outgoings.
2. **Determining Required Gross Income**: Estimating the amount one needs to earn before taxes and savings to maintain the desired lifestyle.
3. **Assessing Additional Income Needed**: Identifying the shortfall between current income and the lifestyle-affordable income.
4. **Evaluating Percentage Increase Needed**: Calculating how much the current income should increase to meet lifestyle expectations.

These calculations assist in setting realistic financial goals and planning effectively for the future.

## Current Functionality

### API Endpoints

- `GET /expenses/`: Retrieve a list of all recorded expenses.
- `POST /expenses/`: Add a new expense record.
- `DELETE /expenses/{expense_id}`: Delete an expense based on its ID.
- `GET /settings/`: Fetch current user settings like tax rate, savings rate, and more.
- `POST /settings/`: Update user settings.
- `GET /required_income/`: Calculate and fetch the required monthly income based on current expenses and settings.

### CLI Commands

- `list_expenses`: Lists all expenses.
- `add_expense [category] [amount] [frequency]`: Adds a new expense entry.
- `delete_expense [expense_id]`: Removes an expense entry by ID.
- `get_settings`: Displays the current user settings.
- `update_settings [tax_rate] [savings_rate] [current_income] [current_expenses]`: Modifies user settings.
- `calculate_required_monthly_income`: Calculates the necessary monthly income to afford the desired lifestyle.

### Installation

`pip install -r requirements.txt`

### Usage

You can either use it via API or with CLI.

`python cli.py --help`

## Examples

#### Listing expenses
![list-expenses](https://github.com/adrian-em/lifestyle-cost-designer/assets/650616/9007d212-cfbd-4d38-af5a-409a53aecfc6) 

#### Updating settings
![update-settings](https://github.com/adrian-em/lifestyle-cost-designer/assets/650616/a4e1ce43-f827-435e-8e17-9875d3d10968)

#### Calculating required income
![calculate-required-income](https://github.com/adrian-em/lifestyle-cost-designer/assets/650616/8f3b7c33-7559-436c-99d2-96e85907ef51)

#### Plotting required income by expense
![plot-required-income](https://github.com/adrian-em/lifestyle-cost-designer/assets/650616/1f4a4f5f-e854-46ae-9db3-5df5b9dd741a)

